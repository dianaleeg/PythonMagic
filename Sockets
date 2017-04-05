#import socket module
#from socket import *
import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 9204))
serverSocket.listen(5)
print"socket created"
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    print 'Got connection from', addr
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = str(f)
        connectionSocket.send("Thanks for connecting")
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        print("404 File Not Found")
        #Close client socket
        connectionSocket.close()
    serverSocket.close() 
