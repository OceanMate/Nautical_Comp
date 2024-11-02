# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:07:49 2024

@author: deant
"""
import socket
from typing import Optional


class CommandClient:
    def __init__(self, robot_ip: str = '172.61.94.163', cmd_port: int = 8000):
        self.robot_ip = robot_ip
        self.cmd_port = cmd_port
        self.cmd_socket: Optional[socket.socket] = None
        self.running = False

    def connect(self) -> None:
        """Establish connection with the server"""
        self.cmd_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Connecting to {self.robot_ip}:{self.cmd_port}...")
        self.cmd_socket.connect((self.robot_ip, self.cmd_port))
        print("Connected!")
        self.running = True

    def disconnect(self) -> None:
        """Close the connection"""
        if self.cmd_socket:
            self.cmd_socket.close()
        self.running = False

    def send_command(self, command: str) -> None:
        """Send a command string to the server"""
        if self.cmd_socket:
            self.cmd_socket.send(command.encode())

    def start(self) -> None:
        """Start the command client with interactive input"""
        try:
            self.connect()
            print("\nEnter space-separated integers for commands (e.g., '90 45 180')")
            print("Enter 'quit' to exit")
            
            while self.running:
                cmd_input = input("> ")
                if cmd_input.lower() == 'quit':
                    self.send_command('quit')
                    break
                self.send_command(cmd_input)
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.disconnect()

if __name__ == "__main__":
    client = CommandClient()
    client.start()
