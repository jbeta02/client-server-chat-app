# client-server-chat-app

## Utilizes Client-Server model over TCP protocol. Uses threads to support communication of multiple clients.

## Features
* JOIN username
  * When a client wants to join the service, it first connects to
  the server using the hostname of the server machine and the port
  number, then sends a JOIN request with the username. If the
  database is “full”, then the server will print out a status message and send a
  “Too Many Users” message to the client. 
* LIST
  * Clients can use the LIST command to get a list of curretly registersed users.
* MESG <username> <some_message_text>
  * Use the MESG command to messasge and individual registered user.
* BCST <some_message_text>
  * broadcast to a message to all registered users. 
* QUIT
  * Quit the service and leave the list of registered users.
* Unrecognized Messages
  * Unregocnized commands will result in "Unkown Message" message sent to the client.


### Example: Members joinning and Alice broadcasting to all members

#### Alex View
![Screenshot 2024-12-18 131726](https://github.com/user-attachments/assets/99c245b8-4a80-4914-aeb9-474716e8b499)


#### Alice View
![Screenshot 2024-12-18 131757](https://github.com/user-attachments/assets/e8fda1c7-d208-4ad6-b3c6-7f7c87390ddb)


#### Bob View
![Screenshot 2024-12-18 131814](https://github.com/user-attachments/assets/af23a006-0903-4be9-943d-233acca9df7c)


#### Server View
![Screenshot 2024-12-18 131841](https://github.com/user-attachments/assets/6a62afb2-eb37-4f3a-9b8c-7677fbc16a60)

