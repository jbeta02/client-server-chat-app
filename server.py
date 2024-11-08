
import socket
import sys
import time

# start and run server
def run_server(port):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM for TCP

    # bind socket to IP address and port info
    server_socket.bind(('0.0.0.0', port))

    # listen indefinitely
    while True:

        # TODO: implement commands and figure out what to do with multiple clients (need threads?)

        # save message and client address once received
        message, client_address = server_socket.recvfrom(2048)

        # parse message and check which command it corresponds to
        message_parts = message.decode().split()

        if len(message_parts) == 1:
            # will be either LIST or QUIT
            if message_parts[0] == "LIST":
                pass

            elif message_parts[0] == "QUIT":
                pass

            else:
                # Unrecognized Messages
                pass

        elif len(message_parts) == 2:
            # will be any of the other commands

            if message_parts[0] == "JOIN":
                pass

            elif message_parts[0] == "MESG":
                pass

            elif message_parts[0] == "BCST":
                pass

            else:
                # Unrecognized Messages
                pass

        else:
            # Unrecognized Messages
            pass


def main():
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    # grab port number from arguments
    port = int(sys.argv[1])

    run_server(port)

# Run your script
if __name__ == "__main__":
    main()