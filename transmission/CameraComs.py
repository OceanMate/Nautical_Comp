import io
import socket
import time
import cv2
from PIL import Image
import threading

class CameraComs:
    def __init__(self, host='localhost', port=46389):
        self.host = host
        self.port = port
        self.cameras, self.cv2_indexes = self.get_available_cameras(max_cameras=2)  # Assuming a maximum of 4 cameras
        self.sockets = {}  # Dictionary to store sockets for each camera

    def get_available_cameras(self, max_cameras, resolution=(640, 480)):
        cameras = []
        cv2_indexes = []
        for i in range(max_cameras):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
                print(f"Camera {i} connected with resolution {resolution[0]}x{resolution[1]}")
                cameras.append(cap)
                cv2_indexes.append(i)
            else:
                cap.release()  # Ensure resources are released for unresponsive cameras
        return cameras, cv2_indexes

    def connect(self, camera_index):
        while True:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.sockets[camera_index] = client_socket
                print(f"Camera {camera_index} connecting to {self.host}:{self.port + camera_index}")
                break
            except socket.error as e:
                print(f"Connection failed for camera {camera_index}: {e}. Retrying in 5 seconds...")
                time.sleep(5)

    def handle_client(self, camera, camera_index, cv2_index):
        self.connect(camera_index)  # Establish connection for this camera
        client_socket = self.sockets[camera_index]
        try:
            while True:
                ret, frame = camera.read()
                if not ret:
                    print(f"Camera {camera_index} frame read failed. Attempting to reinitialize...")
                    camera.release()  # Release the current camera
                    camera = cv2.VideoCapture(cv2_index)  # Reinitialize the camera using the index
                    if not camera.isOpened():
                        print(f"Failed to reinitialize at {cv2_index}. Retrying in 1 second...")
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
                image_data = image_stream.read()
                client_socket.sendto(image_data, (self.host, self.port + camera_index))
        finally:
            print("An error has broken the connection")

    def start(self):
        for index, camera in enumerate(self.cameras):
            threading.Thread(target=self.handle_client, args=(camera, index, self.cv2_indexes[index]), daemon=True).start()