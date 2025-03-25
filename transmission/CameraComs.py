import io
import socket
import struct
import time
import cv2
from PIL import Image
import threading

class CameraComs:
    def __init__(self, host='192.168.1.1', port=46389):
        self.host = host
        self.port = port
        self.cameras = self.get_available_cameras()  # Assuming a maximum of 4 cameras
        self.sockets = {}  # Dictionary to store sockets for each camera

    def get_available_cameras(self):
        cameras = []
        for i in range(5):  # Assuming a maximum of 5 cameras
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print(f"Camera {i} connected")
                cameras.append(cap)
            else:
                print(f"Camera {i} not available")
                cap.release()
        return cameras

    def connect(self, camera_index):
        while True:
            try:
                client_socket = socket.socket()
                client_socket.connect((self.host, self.port))
                connection = client_socket.makefile('wb')
                self.sockets[camera_index] = (client_socket, connection)
                print(f"Connection established for camera {camera_index}")
                break
            except (socket.error, ConnectionRefusedError) as e:
                print(f"Connection failed for camera {camera_index}: {e}. Retrying in 5 seconds...")
                time.sleep(5)

    def handle_client(self, camera, camera_index):
        self.connect(camera_index)  # Establish connection for this camera
        client_socket, connection = self.sockets[camera_index]
        try:
            while True:
                ret, frame = camera.read()
                if not ret:
                    break
                # Resize the frame to reduce data size
                frame = cv2.resize(frame, (640, 480))  # Resize to 640x480
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img)
                image_stream = io.BytesIO()
                # Save with reduced quality to minimize size
                img_pil.save(image_stream, format='JPEG', quality=50)  # Set quality to 50
                image_stream.seek(0)
                image_len = image_stream.getbuffer().nbytes
                connection.write(struct.pack('<L', image_len))
                connection.flush()  # Ensure data is sent immediately
                connection.write(image_stream.read())
                connection.flush()  # Ensure data is sent immediately
        except (socket.error, BrokenPipeError) as e:
            print(f"Connection lost for camera {camera_index}: {e}. Reconnecting...")
            self.connect(camera_index)  # Reconnect if the connection is lost
        finally:
            connection.write(struct.pack('<L', 0))
            connection.flush()  # Ensure the termination signal is sent
            connection.close()
            client_socket.close()
            camera.release()

    def start(self):
        for index, camera in enumerate(self.cameras):
            threading.Thread(target=self.handle_client, args=(camera, index)).start()
# [Warn:1@8.202] global cap_v4l.cpp:803 requestBuffers VIDEOIO(V4L2:/dev/video0): failed VIDIOC_REQBUFS: errno=19 (no such device)