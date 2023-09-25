import socket 


#decide which location we want to visit and take a bag that can hold up to 4096 items 
HOST = "www.google.com"
PORT = 80 
BYTES_TO_READ = 4096 




def get(host, port):

    #we are going to see the main page of the shop (google.com)
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"

    #the customer/client visits and knocks at the foor of the shop (google.com) with ipv4 and tcp to ensure 
    #that the shop owner doesnt forget any of his requests 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((host, port))


    #once we enter the shop we give the shopkeeper our shoppping list / requests 
    #and that we are not going to add more to the list (using the line (s.shutdown()))
    s.send(request)
    s.shutdown(socket.SHUT_WR) #done sending - tell google server / shop keeper

    #the customer receives all the goods and info from the google server/shopkeeper 
    #and keeps filling their bag up till the 4096 item limit and goes back for more 
    #until the google server/shopkeeper says they have given all the good and info from the requests /shopping list
    result = s.recv(BYTES_TO_READ)
    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    #After ensuring they've received everything they needed, the customer politely says goodbye
    # and leaves the shop, ending the shopping trip.
    s.close()

get(HOST, PORT)


