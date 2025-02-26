import io
import socket
import struct
import time
import cv2
from PIL import Image
import threading

class CameraComs:
    def __init__(self, host='172.60.58.193', port=46389):
        self.client_socket = socket.socket()
        self.client_socket.connect((host, port))
        self.connection = self.client_socket.makefile('wb')
        self.cameras = self.get_available_cameras()  # Assuming a maximum of 4 cameras
        
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
        try:
            while True:
                ret, frame = camera.read()
                if not ret:
                    break
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img)
                image_stream = io.BytesIO()
                img_pil.save(image_stream, format='JPEG')
                image_stream.seek(0)
                image_len = image_stream.getbuffer().nbytes
                self.connection.write(struct.pack('<L', image_len))
                self.connection.write(image_stream.read())
                time.sleep(0.01)
                
        finally:
            self.connection.write(struct.pack('<L', 0))
            self.connection.close()
            self.client_socket.close()
            camera.release()

    def start(self):
        for camera in self.cameras:
            threading.Thread(target=self.handle_client, args=(camera,)).start()