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
  print("\Available commands:")
  print("JOIN <username> - Join server with username")
  print("LIST - Get list of registered clients")
  print("MESG <username> <mesg> - Send a message to a specific user")
  print("BCST <message> - Broadcast a message to all registered clients")
  print("QUIT - Leave the server")

command = input("Enter command: ").strip()
serv_sock.send(command.encode('ascii'))

data = serv_sock.recv(1024)
print('Received from server: ', data.decode('ascii'))

if command.upper().startswith("QUIT"):
  print("Disconnected from server.")
  break

serv_sock.close()

if __name__ == '__main__':
  main()
