import socket
import csv
import pickle
import video as vd
import random



video_ptr=[]
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

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

cr=csv.reader(open("transcoding_mesurment.tsv"),delimiter="\t")
#c=csv.writer(file("server_pred4.tsv","w+"))

cr = list(cr)

temp = []
for i in range(10):
	number = random.randint(0,60000)
	row = cr[number]
	temp.append(vd.video_request(row[0],row[5],row[4],row[3],row[10],row[6],row[2],row[7],row[9],row[8],row[11],row[12],row[13],row[16],row[17],row[19],row[18],row[15]))



for i in temp:
	print i.request()

for vi in temp:
        #print('receiving data...')
        
        data_id=pickle.dumps(vi)
       
        s.sendall(data_id)
       

#print('Successfully get the file')
#csv.writer(file("client_rev.tsv", 'w+'), delimiter="\t").writerows(csv.reader(open("received_file.csv")))
s.close()
print('connection closed')
