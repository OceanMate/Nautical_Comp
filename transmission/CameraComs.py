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
        self.cameras, self.cv2_indexes = self.get_available_cameras()  # Assuming a maximum of 4 cameras
        self.sockets = {}  # Dictionary to store sockets for each camera

    def get_available_cameras(self):
        cameras = []
        cv2_indexes = []
        for i in range(5):  # Assuming a maximum of 5 cameras
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                # Set the resolution to 640x480
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                print(f"Camera {i} connected with resolution 640x480")
                cameras.append(cap)
                cv2_indexes.append(i)
            else:
                print(f"Camera {i} not available")
                cap.release()
        return cameras, cv2_indexes

    def connect(self, camera_index):
        while True:
            try:
                client_socket = socket.socket()
                client_socket.connect((self.host, self.port + camera_index))  # Use unique port for each camera
                connection = client_socket.makefile('wb')
                self.sockets[camera_index] = (client_socket, connection)
                print(f"Connection established for camera {camera_index}")
                break
            except (socket.error, ConnectionRefusedError) as e:
                print(f"Connection failed for camera {camera_index}: {e}. Retrying in 5 seconds...")
                time.sleep(5)

    def handle_client(self, camera, camera_index, cv2_index):
        self.connect(camera_index)  # Establish connection for this camera
        client_socket, connection = self.sockets[camera_index]
        try:
            while True:
                ret, frame = camera.read()
                if not ret:
                    print(f"Camera {camera_index} frame read failed. Attempting to reinitialize...")
                    camera.release()  # Release the current camera
                    camera = cv2.VideoCapture(cv2_index)  # Reinitialize the camera using the index
                    if not camera.isOpened():
                        print(f"Failed to reinitialize camera {camera_index}. Retrying in 1 second...")
                        time.sleep(1)  # Wait before retrying
                        continue
                    print(f"Camera {camera_index} successfully reinitialized.")
                    continue
                # Resize the frame to reduce data size
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
        finally:
            print("An error has broken the connection")

    def start(self):
        for index, camera in enumerate(self.cameras):
            threading.Thread(target=self.handle_client, args=(camera, index, self.cv2_indexes[index]), daemon=True).start()