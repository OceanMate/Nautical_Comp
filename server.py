# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:27:04 2024

@author: deant
"""

# server.py
import socket
import signal
import sys
from typing import List, Optional

class ROVServer:
    
    _instance = None

    # When a new instance is created, sets it to the same global instance
    def __new__(cls):
        # If the instance is None, create a new instance
        # Otherwise, return already created instance
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._start()
        return cls._instance
    
    
    def _start(self):
        self.port = 8000
        self.is_connected = False
        self.shutdown = False
        self.motor_data: List[float] = [0,0,0,0,0,0]
        
        self.socket = socket.socket()
        self.socket.setblocking(False)  # Set the socket to non-blocking mode
        self.socket.listen(1)
    
    def connect_to_server(self):
        # Start the ROV server
        try:
            self.socket.connect(('localhost', self.port))
            self.is_connected = True
        except BlockingIOError:
            pass
        except socket.error as e:
            print(f"Server failed to start: {e}")
            self.is_connected = False
    
    def disconnect(self):
        # Need to add code to stop all motors before shutting down
        self.is_connected = False
        try:
            self.socket.close()
        except socket.error:
            pass
        finally:
            print("Server stopped")
    
    def process_command(self, data: str):
        print(f'Received data: {data}')
        
        parts = data.split()
        if not parts:
            return
            
        cmd_type = parts[0].lower()
        
        if cmd_type == 'quit':
            self.disconnect()
            self.shutdown = True
            return
            
        if cmd_type == 'motors' and len(parts) > 1:
            try:
                values = [float(x) for x in parts[1:]]
                # Store motor values and apply them
                self.motor_data = values
                print(f'Received motor values: {values}')
            except ValueError:
                print('Invalid motor values received')
    
      
    def update(self):        
        if not self.is_connected:
            self.connect_to_server()            
        
        if self.is_connected:
            try:
                data = self.socket.recv(1024).decode().strip()
                if data:
                    self.process_command(data)
            except BlockingIOError:
                pass  # No data received yet
            except socket.error as e:
                print(f"Connection error: {e}")
                self.is_connected = False