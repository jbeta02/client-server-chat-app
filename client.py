import sys
import socket

def main():
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    connection_status = serv_sock.connect_ex((host, port))
    if connection_status != 0:
        print("Unable to connect to the server")
        sys.exit(1)
    else:
        print("Connected to the server")

    joined = False
    username = ""

    while True:
        if not joined:
            command = input("Enter JOIN followed by your username: ")
            if command.startswith("JOIN"):
                username = command.split()[1]
                serv_sock.send(command.encode('ascii'))
                response = serv_sock.recv(1024).decode('ascii')
                print(response)
                if "joined" in response:
                    joined = True
            else:
                print("You must join first with the command: JOIN <username>")
        else:
            command = input("")
            serv_sock.send(command.encode('ascii'))

            if command.startswith("MESG"):
                recipient = command.split()[1]
                message = ' '.join(command.split()[2:])
                print(f"MESG {recipient}: {message}")

            elif command.startswith("BCST"):
                message = ' '.join(command.split()[1:])
                print(f"{username} is sending a broadcast")
                print(f"{username}: {message}")

            elif command == "LIST":
                print("LIST")

            elif command == "QUIT":
                print(f"{username} is quitting the chat server")
                joined = False
                serv_sock.close()
                break

            response = serv_sock.recv(1024).decode('ascii')
            print(response)

if __name__ == '__main__':
    main()
