import random
import time
import sys
from termcolor import colored
import socket
import struct


class SocketArduinoMouse:
    def sendMouseCoordinates(self, x, y):
        try:
            # Create a socket
            sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set up the server address
            server_addr = ("0.0.0.0", 1337)  # Arduino IP address and port number
            
            # Connect to the server
            sockfd.connect(server_addr)
            
            # Send mouse coordinates
            final_x = int(x)
            final_y = int(y)
            
            # Only try to move mouse if we're actually moving more than 0 pixels
            if final_x != 0 or final_y != 0:
                buffer = struct.pack("bb", final_x, final_y)
                sockfd.send(buffer)
        finally:
            sockfd.close()
