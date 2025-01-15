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
    def __init__(self, port: int = 8000):
        self.port = port
        self.socket = None
        self.running = False
        self.command_data: Dict[str, List[float]] = {}
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.handle_shutdown)
        signal.signal(signal.SIGTERM, self.handle_shutdown)
    
    def handle_shutdown(self, signum, frame):
        """Handle shutdown signals gracefully"""
        print("\nShutdown signal received")
        self.stop()
    
    def start(self) -> None:
        """Start the ROV server"""
        try:
            self.socket = socket.socket()
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(('0.0.0.0', self.port))
            self.socket.listen(1)
            self.socket.settimeout(0.00001)  # 1 second timeout for accept()
            self.running = True
            self.shutdown = False
            self.linear_motor_speeds: List[float] = [0,0,0,0]
            self.vertical_motor_speeds: List[float] = [0,0]
            print(f'ROV Server listening on port {self.port}...')
            
            self.run_server()
            
        except socket.error as e:
            print(f"Server failed to start: {e}")
            self.stop()
    
    def stop(self) -> bool:
        """Stop the ROV server gracefully"""
        # Need to add code to stop all motors before shutting down
        self.running = False
        if self.socket:
            try:
                self.socket.close()
            except socket.error:
                pass
            finally:
                self.socket = None
                self.shutdown = True
                return self.shutdown
    
    def process_command(self, data: str) -> None:
        """Process received command"""
        parts = data.split()
        if not parts:
            return
            
        cmd_type = parts[0].lower()
        
        if cmd_type == 'quit':
            self.running = False
            return
            
        if cmd_type == 'l_motors' and len(parts) > 1:
            try:
                values = [float(x) for x in parts[1:]]
                # Store motor values and apply them
                linear_motor_speeds = values
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
      
    def run_server(self) -> None:
        """Main server loop"""
        try:
            conn, addr = self.socket.accept()
            print(f'Connected to {addr}')
            
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

if __name__ == "__main__":
    server = ROVServer()
    server.start()
    while True:
        #print(f"am here")
        server.run_server()

