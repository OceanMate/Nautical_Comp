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
        self.client_socket = None
        self.connection = None
        self.cameras = self.get_available_cameras()  # Assuming a maximum of 4 cameras

    def connect(self):
        while True:
            try:
                self.client_socket = socket.socket()
                self.client_socket.connect((self.host, self.port))
                self.connection = self.client_socket.makefile('wb')
                print("Connection established")
                break
            except (socket.error, ConnectionRefusedError) as e:
                print(f"Connection failed: {e}. Retrying in 5 seconds...")
                time.sleep(5)

    def get_available_cameras(self):
        cameras = []
        for i in range(5):  # Assuming a maximum of 5 cameras
            cap = cv2.VideoCapture(i)
            if cap is not None and cap.isOpened():
                print(f"Camera {i} connected")
                cameras.append(cap)
            else:
                cap.release()
        return cameras

    def handle_client(self, camera):
        while True:
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
                    self.connection.write(struct.pack('<L', image_len))
                    self.connection.flush()  # Ensure data is sent immediately
                    self.connection.write(image_stream.read())
                    self.connection.flush()  # Ensure data is sent immediately
            except (socket.error, BrokenPipeError) as e:
                print(f"Connection lost: {e}. Reconnecting...")
                self.connect()  # Reconnect if the connection is lost
            finally:
                if self.connection:
                    self.connection.write(struct.pack('<L', 0))
                    self.connection.flush()  # Ensure the termination signal is sent
                    self.connection.close()
                if self.client_socket:
                    self.client_socket.close()
                camera.release()

    def start(self):
        self.connect()  # Establish initial connection
        for camera in self.cameras:
            threading.Thread(target=self.handle_client, args=(camera,)).start()