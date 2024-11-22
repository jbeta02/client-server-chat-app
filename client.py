import sys
import socket
import threading


# use thread to listen to server to allow the usage of input() while the server response is printed
def listen_to_server(sock):
    while True:
        response = sock.recv(1024).decode('ascii')
        if not response:
            print("Server closed the connection.")
            break
        print(response)

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

    # start thread and listen for server responses
    listener_thread = threading.Thread(target=listen_to_server, args=(serv_sock, ))
    listener_thread.daemon = True
    listener_thread.start()

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

            if command == "QUIT":
                print(f"{username} is quitting the chat server")
                serv_sock.close()
                break

    sys.exit(0)


if __name__ == '__main__':
    main()
