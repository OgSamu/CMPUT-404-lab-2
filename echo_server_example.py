#the host 127.0.01 is same as localhost 



#setting up the shop for the client to visit us 

# .bind(): Set up the shop's location and door.

# .listen(): Open the shop's door for business and wait for customers.

import socket 

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # The .bind() method helps your program claim a specific 'spot' on your computer, 
    # so other devices know where to find it and connect to it

    # Once your server binds to a particular HOST and PORT, it's like putting up a
    #  sign that says, "I'm here and ready to accept connections on this address
    #  and this door number."
    s.bind((HOST, PORT))


    #1. This is the first socket we create 
    # ------it makes the server into a listening socket to accept new connections 
    s.listen()
    #-------------


    #2. This is the second socket we create 
    # ------we use this socket to communicate with the client 

    #this is a very popular shop so each time a customer enters the server sets up a
    #  dedicated checkout lane just for that customer - this way each customer get individual attention 
    #and the transactions are smooth 

    # method is the server's way of acknowledging incoming clients and 
    # setting up a dedicated communication line with each of them.
    conn, addr = s.accept()

    #---------------------------
    with conn:
         #the shopkeeper is nothign the specific custoemr he is talking to 
        print(f"connected by {addr}") 
        
        #the shopkeeper is going to keep listening to the request of that specific customer 
        # until the customer decides they are done shopping 
        while True:
            
            #specifically where the shopkeeper notes down whatever the customer says  
            #The number 1024 specifies how big the list can be (in bytes) at a time.
            #------------------------Example------------------------------
            # It's like the shopkeeper saying, "Tell me up to 1024 items you want,
            #  and then if you have more, we'll continue."
            data = conn.recv(1024)

            #If the customer doesn't give any list or says they're done shopping 
            # (i.e., sends no data), the shopkeeper understands that the interaction
            #  is over. The customer is done, and it's time to close the counter for that customer. 
            if not data:
                break

            #After listening to the customer's request, the shopkeeper (server) confirms back by 
            # repeating the list to ensure they got it right. This is like an echo, where the server 
            # sends back exactly what the client sent.

            #-----------------------------example----------------------------------
            #It's as if the customer gives a list of items, and the shopkeeper repeats the list back,
            #  saying, "Alright, I've got your list. Here's what you asked for."
            conn.sendall(data)


