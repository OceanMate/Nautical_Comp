import socket

SERVER_IP = '192.168.1.1'  # IP address of the server computer
PORT = 65432               # Must match the server's port

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

# Send a message
message = "Hello, Server!"
client_socket.sendall(message.encode())

# Receive response
data = client_socket.recv(1024)
print("Server replied:", data.decode())

client_socket.close()
