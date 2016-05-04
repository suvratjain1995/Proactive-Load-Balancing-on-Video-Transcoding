# Routing python file will call server based on their availability
 
import random
import socket
import bluelet
import pickle
import video as vd
import i_am_testing as ml
import numpy as np


"""
class video(object):
	
	def __init__(self,id,duration,bitrate,bitrate_video,height,width,frame_rate,codec):
		self.id = id
		self.duration = duration
		self.bitrate = bitrate
		self.bitrate_video = bitrate_video
		self.height = height
		self.width = width
		self.frame_rate = frame_rate
		self.codec = codec
		
	def v_id(self):
		return self.id
	def v_codec(self):
		return self.codec
"""


def echoer(conn):

        data = yield conn.recv(1024)
        data1.append(pickle.loads(data))
        #print(l.id)
        while data:
            data = yield conn.recv(1024)
            if not data:
                break
            data1.append(pickle.loads(data))
            #print(l.id)
            
#Task types (templates for periodic tasks)
class TaskType(object):

    #Constructor
    def __init__(self,execution,name):
        """
        self.period    = period
        self.release   = release
        self.deadline  = deadline
        """
        self.execution = execution
        self.name      = name


class Server:


    def __init__(self,capacity,occ,port,name):
        self.capacity   = capacity
        self.port       = port
        self.name       = name.replace("\n", "")
        self.occupied   = occ
        self.available  = capacity-occ      # initially available is capacity as none of the slot has been used yet
        self.id         = int(random.random() * 10000)

    def avail(self):
        return self.available

    def port_num(self):
        return self.port

    def assign(self,time):
        if self.available >= time:       # weighted transcoding time is assigned to server
            self.occupied += time
            self.available -= time
            return True
        else:
            return False

    #Get name as Name + # + id ; Random id for every Server
    def get_unique_name(self):
        return str(self.name) + "#" + str(self.id)

        
def capacity_cmp(self, other):
    if self.available < other.available:
        return 1
    if self.available > other.available:
        return -1
    return 0



if __name__ == '__main__':
    
    
    host = socket.gethostname()  # '127.0.0.1' can also be used
    serverfile = open('server.txt')
    lines = serverfile.readlines()
    taskfile = open('test.txt')
    tlines = taskfile.readlines()

    server_s = []
    task_types = []
    
    data1 = []
    
    bluelet.run(bluelet.server('', 9001, echoer))
    
    for line in lines:
        line = line.split(' ')
        for i in range (0,3):
            line[i] = int(line[i])
        if len(line) == 4:
            name = line[3]
        elif len(line) == 3:
            name = 'Server'
        else:
            raise Exception('Invalid Server.txt file structure')
        if int(line[0])>0:
            server_s.append(Server(capacity=line[0], occ=line[1], port=line[2], name=name))
    
    temp2 = []
    for i in data1:
    	temp2.append(i.request())
    	
    y_rbf = ml.machine_learn(temp2)
    for i in range(len(y_rbf)):
	print str(y_rbf[i])

    y_rbf = y_rbf.tolist()

    task_id = []
    task_time = []
    for i in data1:
    	task_id.append(i.id)
    for i in range(len(y_rbf)):
    	task_time.append(float(y_rbf[i]))
    
    for i in range(len(task_id)):
    	
        task_types.append(TaskType(task_time[i],task_id[i]))
        
      
    server_s = sorted(server_s, capacity_cmp)
    #print "Sorted"
    server_assign = server_s[0]

    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for tline in task_types:
        for s in server_s:
            if s.available > server_assign.available:
                server_assign = s
            
                
        if(server_assign.assign(tline.execution)):
            print tline.name+" assigned to Server : "+server_assign.get_unique_name()
            #port = server_assign.port
            port = server_assign.port
            #9999
            # Creating the socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #Connecting to socket
            sock.connect((host, port)) 
            #connect takes tuple of host and port
            #data = sock.recv(1024)
            #print "hello this is data "+data
            msg =str(tline.execution) +" "+ tline.name
            msg += "\n"
            print msg
            sock.send('HI! I am client. '+msg)
            sock.close()
        else:
            print "All the servers are busy please try after some time"
                        
