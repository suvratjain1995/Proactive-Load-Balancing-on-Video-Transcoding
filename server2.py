import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= socket.gethostname()

port=8082

serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serversocket.bind((host,port))
serversocket.listen(5)

while True:
	clientsocket,addr=serversocket.accept()
	print("got connection %s"%str(addr))
	rec=clientsocket.recv(1024)
	print rec
	currenttime=time.ctime(time.time())+ "\r\n"
	clientsocket.send(currenttime.encode('ascii'))
	clientsocket.close()

