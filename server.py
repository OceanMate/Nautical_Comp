# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:27:04 2024

@author: deant
"""

# server.py
import socket
import signal
import sys
from typing import Dict, List, Optional

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
    
    def _start(self, port: int = 8000):
        self.port = port
        self.socket = None
        self.running = False
        self.command_data: Dict[str, List[float]] = {}
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.handle_shutdown)
        signal.signal(signal.SIGTERM, self.handle_shutdown)
                
        """Start the ROV server"""
        try:
            self.socket = socket.socket()
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(('0.0.0.0', self.port))
            self.socket.listen(1)
            self.socket.settimeout(0.00001)  # 1 second timeout for accept()
            self.isEnabled = False
            self.linear_motor_speeds: List[float] = [0,0,0,0]
            self.vertical_motor_speeds: List[float] = [0,0]
            print(f'ROV Server listening on port {self.port}...')
            
            
        except socket.error as e:
            print(f"Server failed to start: {e}")
            self.stop()
    
    def handle_shutdown(self, signum, frame):
        """Handle shutdown signals gracefully"""
        print("\nShutdown signal received")
        self.stop()        
    
    def stop(self) -> bool:
        """Stop the ROV server gracefully"""
        # Need to add code to stop all motors before shutting down
        if self.socket:
            try:
                self.socket.close()
            except socket.error:
                pass
            finally:
                self.socket = None
                return self.shutdown
    
    def process_command(self, data: str) -> None:
        """Process received command"""
        parts = data.split()
        if not parts:
            return
            
        cmd_type = parts[0].lower()
        
        if cmd_type == 'isEnabled':
            self.isEnabled = parts
            return
            
        if cmd_type == 'l_motors' and len(parts) > 1:
            try:
                values = [float(x) for x in parts[1:]]
                # Store motor values and apply them
                self.linear_motor_speeds = values
                print(f'Received motor values: {values}')
            except ValueError:
                print('Invalid motor values received')
        elif cmd_type == 'vert_motors' and len(parts) > 1:
            try:
                values = [float(x) for x in parts[1:]]
                # Store motor values and apply them
                vertical_motor_speeds = values
                print(f'Received motor values: {values}')
            except ValueError:
                print('Invalid motor values received')
      
    def update(self) -> None:
        """Main server loop"""
        try:
            conn, addr = self.socket.accept()
            #print(f'Connected to {addr}')
            
            conn.settimeout(5)  # 5 seconds for timeout
            
            try:
                data = conn.recv(1024).decode().strip()
                if not data:
                    return
                
                self.process_command(data)
                
            except socket.timeout:
                return
            except socket.error as e:
                print(f"Connection error: {e}")
                return
            
            #conn.close()
            
        except socket.timeout:
            return
        except socket.error as e:
            print(f"Server error: {e}")
            if self.running:
                print("Waiting for new connections...")
    
    def get_latest_command(self, cmd_type: str) -> Optional[List[float]]:
        """Get the latest values for a command type"""
        return self.command_data.get(cmd_type)


