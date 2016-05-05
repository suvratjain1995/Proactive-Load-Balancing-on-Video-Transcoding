import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV
##############################################################
import csv
import random_train_data as rtd

def machine_learn(test_data):
	if False:
	
		cr=csv.reader(open("server_pred2.tsv"))
		data = list(cr)
		tr= csv.reader(open("server_pred3.tsv"))
		data2= list(tr)
		print "i am printing whats coming from load balancer"
		print test_data
		#print len(data)

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
		"""
		test_trans_time = []
		test_data = []
		"""
		train_trans_time = trans_time[:300]

		#print test_trans_time

		train_data = data[1:301]

		#print train_data

		#print test_data

		"""
		test_trans_time = trans_time[301:340]
		test_data = data[302:341]
		"""
	
	
	train_data,train_trans_time = rtd.want_train_data()
	train_data = np.array(train_data)
	train_trans_time = np.array(train_trans_time)
	
	test_data = np.array(test_data)
	#train_data = preprocessing.scale(train_data)
	#print test_data
	scalar = preprocessing.StandardScaler().fit(train_data)
	train_data = scalar.transform(train_data)

	test_data = scalar.transform(test_data)

	#print test_data

	#print train_data
	#print test_data

	svr_rbf = SVR(kernel='rbf' ,C = 1e3 , gamma = 1)
	y_rbf = svr_rbf.fit(train_data, train_trans_time).predict(test_data)
	
	"""
	for i in range(len(y_rbf)):
		print str(y_rbf[i]) + " " + str(test_trans_time[i])
	"""
	"""
	print len(train_trans_time)
	print len(train_data)
	print len(test_trans_time)
	print len(test_data)
	"""
	return y_rbf
