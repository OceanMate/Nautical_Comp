# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:05:39 2024

@author: deant
"""

# min_server.py
import socket

def run_server(port=8000):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    print('Waiting for connection...')
    
    conn, addr = s.accept()
    print('Connected to', addr)
    
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data or data == 'quit': break
            try:
                values = [int(x) for x in data.split()]
                print('Got:', values)
            except:
                print('Invalid input')
    finally:
        conn.close()
        s.close()

if __name__ == "__main__":
    run_server()