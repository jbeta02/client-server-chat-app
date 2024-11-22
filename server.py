
import socket
import sys
import threading

# get data from client
def handle_cli_messages(cli_socket, users):
    client_username = ""
    while True:
        # get message from client
        message = cli_socket.recv(1024)

        # client disconnected so stop listening to this client
        if not message:
            print('Disconnecting')
            break

        # parse message and check which command it corresponds to
        message_parts = message.decode().split()

        if len(message_parts) == 1:
            # will be either LIST or QUIT
            if message_parts[0] == "LIST":
                if client_username != "": # check if user is registered
                    user_list = ""
                    first = True
                    for user in users:
                        if first:
                            user_list += user[0]
                            first = False
                        else:
                            user_list += ", " + user[0]

                    cli_socket.send(user_list.encode("ascii"))

            elif message_parts[0] == "QUIT":
                # leave loop and close socket
                #TODO remove user from users list
                users.remove((client_username, cli_socket))
                break

            else:
                # Unrecognized Messages
                cli_socket.send("Unknown Message".encode("ascii"))

        elif len(message_parts) == 2:
            # will be JOIN or BCST command

            if message_parts[0] == "JOIN":
                # check if user list is full
                if len(users) >= 10:
                    cli_socket.send("Too Many Users".encode("ascii"))

                # check if user already joined
                if (message_parts[1], cli_socket) in users:
                    cli_socket.send("Already Joined".encode("ascii"))

                # add user to users
                else:
                    # send user spacial join message
                    cli_socket.send((message_parts[1] + " joined!Connected to server!").encode('ascii')) # message_parts[1] will be the username
                    send_to_all(users, message_parts[1] + " joined!") # message_parts[1] will be the username
                    # add user to users
                    users.append((message_parts[1], cli_socket))
                    client_username = message_parts[1]

            elif message_parts[0] == "BCST":
                if client_username != "": # check if user is registered
                    # message for sender
                    cli_socket.send((client_username + " is sending a broadcast").encode("ascii"))
                    # message to all users
                    send_to_all(users, client_username + ": " + message_parts[1]) # message_parts[1] will be the message

            else:
                # Unrecognized Messages
                cli_socket.send("Unknown Message".encode("ascii"))


        elif len(message_parts) > 3: # MESG username [message]
            # will be MESG

            if message_parts[0] == "MESG":
                # build string message
                string = ""
                for i in range(2, len(message_parts)):
                    string += " " + message_parts[i]

                # determine who to send to
                for user in users:
                    if user[0] == message_parts[1]:
                        # send message to "target user" from "user list" using "target user's" socket
                        user[1].send((client_username + ": " + string.strip()).encode("ascii"))

            else:
                # Unrecognized Messages
                cli_socket.send("Unknown Message".encode("ascii"))

        else:
            # Unrecognized Messages
            cli_socket.send("Unknown Message".encode("ascii"))

    cli_socket.close()

def send_to_all(users, message):
    for user in users:
        user[1].send(message.encode("ascii"))


def parse_command(input, inputs):

    if inputs == 1:
        return (input[:4], "", "")

    elif inputs == 2:
        input_parts = input.split()
        return (input_parts[0], input_parts[1], "")

    elif inputs == 3:

        # get command name
        command = input[:4]
        # get new input substring after space
        input_new = input[5:]

        # get first input
        next_space = input_new.index(" ")
        input0 = input_new[:next_space]

        # get second input
        input1 = input_new[next_space + 1:]

        return (command, input0, input1)

    else:
        return ("", "", "")

# start and run server
def run_server(port):

    # track user list : [(username, client_socket)...]
    users = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM for TCP

    # bind socket to IP address and port info
    server_socket.bind(('0.0.0.0', port))

    # put the socket into listening mode
    server_socket.listen(5)

    # listen indefinitely
    while True:

        # establish connection with client
        cli_socket, addr = server_socket.accept()

        # setup thread
        thread = threading.Thread(target=handle_cli_messages, args=(cli_socket, users,))
        # start thread
        thread.daemon = True
        thread.start()


    server_socket.close()


def main():
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    # grab port number from arguments
    port = int(sys.argv[1])

    # start and run server
    run_server(port)

# Run your script
if __name__ == "__main__":
    main()