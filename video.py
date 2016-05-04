
import csv


cr=csv.reader(open("server_pred2.tsv"))
data = list(cr)
	#print len(data)

codec = []

for i in range(1,len(data)):
	codec.append(data[i][12])

codec = list(set(codec))

def convert(s):
	for i in range(len(codec)):
		if codec[i] == s:
			return i
	
	

class video_request(object):
	
	def __init__(self,id,bitrate,height,width,frame,frame_rate,codec,i_fr,b_fr,p_fr,i_size,p_size,b_size,o_bitrate,o_framerate,o_height,o_width,o_codec):
		self.id = id
		self.bitrate = float(bitrate)
		self.height = float(height)
		self.width = float(width)
		self.frame= float(frame)
		self.frame_rate = float(frame_rate)
		self.codec = convert(codec)
		self.i_fr=float(i_fr)
		self.b_fr=float(b_fr)
		self.p_fr=float(p_fr)
		self.i_size=float(i_size)
		self.p_size=float(p_size)
		self.b_size=float(b_size)
		self.o_bitrate=float(o_bitrate)
		self.o_framerate=float(o_framerate)
		self.o_height=float(o_height)
		self.o_width=float(o_width)
		self.o_codec=convert(codec)
		
	def request(self):
		temp = [self.codec,self.width,self.height,self.bitrate,self.frame_rate,self.i_fr,self.p_fr,self.b_fr,self.frame,self.i_size,self.p_size,self.b_size,self.o_codec,self.o_bitrate,self.o_framerate,self.o_width,self.o_height]
		return temp
		
	
