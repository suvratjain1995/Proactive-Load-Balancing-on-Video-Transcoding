import csv
import random

def want_train_data():
	cr=csv.reader(open("server_pred2.tsv"))
	data = list(cr)
	tr= csv.reader(open("server_pred3.tsv"))
	data2= list(tr)
	codec = []

	for i in range(1,len(data)):
		codec.append(data[i][12])

	codec = list(set(codec))

	for i in range(1,len(data)):
		for j in range(len(codec)):
			if data[i][0]==codec[j] :
				data[i][0]=j
			if data[i][12] == codec[j]:
				data[i][12] = j
		for j in range(17):
			data[i][j]=float(data[i][j])

	for i in range(1,len(data2)):
		data2[i][0]=float(data2[i][0])

	trans_time = [] 
	for i in range(1,len(data2)):
		trans_time.append(data2[i][0])
	
	train_data = []	
	train_trans_time = []
	for i in range(1000):
		temp = random.randint(1,60000)
		train_data.append(data[temp])
		train_trans_time.append(trans_time[temp-1])
	
	return train_data,train_trans_time
		
		
		
