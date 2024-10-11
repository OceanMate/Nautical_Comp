import socket

class receive_commands:
    _instance = None
    
    # When a new instance is created, sets it to the same global instance
    def __new__(cls):
        # If the instance is None, create a new instance
        # Otherwise, return already created instance
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.start_server()
        self.shutdown = False
        self.motorData = []

    def start_server(host='0.0.0.0', port=12345):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Server listening on {host}:{port}")

    def requstCommands(self):
        conn, addr = self.s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                command = data.decode('utf-8')
                print(f"Received command: {command}")
                
                # Process the command (replace with our actual command handling)
                #response = f"Executing command: {command}"
                #conn.sendall(response.encode('utf-8'))
                
                # First word of command is the type of command
                type = self.getFirstWord(command)
                # Update the data stored in this class
                self.updateData(type, command)




    def getFirstWord(self, string):
        return string.spilt()[0] if string else ''
    
    def updateData(self, type, command):
        if type == "motor":
            # Split the data part of command into a list of motor data
            self.motorData = command.split()[1:]
        elif type == "shutdown":
            self.shutdown = True
        else:
            print("Invalid command type")
