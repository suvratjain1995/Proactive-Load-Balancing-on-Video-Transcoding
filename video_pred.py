import video as vd
import csv	
import random
cr=csv.reader(open("transcoding_mesurment.tsv"),delimiter="\t")
#c=csv.writer(file("server_pred4.tsv","w+"))

cr = list(cr)

temp = []
for i in range(10):
	number = random.randint(0,60000)
	row = cr[number]
	temp.append(vd.video_request(row[0],row[5],row[4],row[3],row[10],row[6],row[2],row[7],row[9],row[8],row[11],row[12],row[13],row[16],row[17],row[19],row[18],row[15]))

for i in temp:
	print i.id

	
	
