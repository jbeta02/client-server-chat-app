import socket
import sys

def main():
  if len(sys.argv) != 3:
    print("Usage: python client.py <server_ip> <server_port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_sock.connect((host, port))
print("Connected to server.")

while True:
  
