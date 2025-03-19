#!/usr/bin/env python3

import selectors
import socket
import threading
import traceback
import psutil

import transmission.libserver as libserver


class ComsThread:
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
        self.sel = selectors.DefaultSelector()
        self.sensor_data = {"IMU": (0.0, 0.0, 0.0)}
        self.robot_state = {"horizontal_motors": (0, 0, 0, 0), "vertical_motors": (0, 0), "enabled": False}
        
        # Get the IP address of the machine
        self.host = self._get_ethernet_ip()  # Use the function to get the IP address
        
        self.port = 65432 # doesn't matter what this value is, as long as it matches landlubber
        
    def _get_ethernet_ip(self):
        """Retrieve the IP address of any active network with 'Ethernet' in its name."""
        try:
            addresses = psutil.net_if_addrs()
            stats = psutil.net_if_stats()

            for intface, addr_list in addresses.items():
                # Check if the interface is up and contains 'Ethernet' in its name
                if intface in stats and stats[intface].isup and "Ethernet" in intface:
                    for addr in addr_list:
                        # Ensure it's an IPv4 address and not a link-local address (169.254.x.x)
                        if addr.family == socket.AF_INET and not addr.address.startswith("169.254"):
                            print(f"Found active interface: {intface} with IP {addr.address}")
                            return addr.address

            raise RuntimeError("No active interface found with 'Ethernet' in its name")
        except Exception as e:
            print(f"Error retrieving Ethernet IP: {e}")
            return "127.0.0.1"  # Fallback to localhost if no Ethernet IP is found
    
    def set_IMU_data(self, xyz : tuple):
        self.sensor_data["IMU"] = xyz
        
    def get_horizontal_motors(self):
        return self.robot_state["horizontal_motors"]
    
    def get_vertical_motors(self):
        return self.robot_state["vertical_motors"]
    
    def get_enabled(self):
        return self.robot_state["enabled"]

    def begin_thread(self):
        thread = threading.Thread(target=self._run_server_socket)
        thread.daemon = True
        thread.start()

    def _accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        message = libserver.Message(self.sel, conn, addr, self.robot_state, self.sensor_data)
        self.sel.register(conn, selectors.EVENT_READ, data=message)
    
    def _run_server_socket(self):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((self.host, self.port))
        lsock.listen()
        print(f"Listening on {(self.host, self.port)}")
        lsock.setblocking(False)
        self.sel.register(lsock, selectors.EVENT_READ, data=None)
        
        try:
            while True:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self._accept_wrapper(key.fileobj)
                    else:
                        message = key.data
                        try:
                            message.process_events(mask, self.sensor_data)
                            # print(f"Received: {message.robot_state}") # Debugging
                            self.robot_state = message.robot_state
                        except Exception:
                            print(
                                f"Main: Error: Exception for {message.addr}:\n"
                                f"{traceback.format_exc()}"
                            )
                            message.close()
        except KeyboardInterrupt:
            print("Caught keyboard interrupt, exiting")
        finally:
            self.sel.close()
