import socket 



#Before going to the shop, the customer (client) decides which shop (server) to visit. 
# They choose the shop located at address HOST and door number PORT. 
# The address 127.0.0.1 indicates that the shop they want to visit is on their own street (i.e., their own computer).
HOST = "127.0.0.1"
PORT = 65432 

#The customer walks to the shop's address and knocks on the door specified by the door number (PORT). 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # The s.connect((HOST, PORT)) line represents the customer (client) trying to enter the shop (server) 
    # at the given address and door.
    s.connect((HOST, PORT))

    # Once inside, the customer hands over a note to the shopkeeper saying, "Hello world". 
    # This is what s.sendall(b"Hello world") does.
    s.sendall(b"Hello world")

    #After giving the note, the customer waits to see if the shopkeeper has a reply.
    #  The customer is ready to listen to a message (or a response) from the shopkeeper 
    # that's up to 1024 bytes long. That's what the line data = s.recv(1024) represents
    data = s.recv(1024)


#After the interaction, as the customer walks away from the shop, they look at the reply 
# they received from the shopkeeper and think about it.
#  Here, the customer is simply printing out (or reflecting upon) the message they received from the shopkeeper.
print(f"Received {data!r}")