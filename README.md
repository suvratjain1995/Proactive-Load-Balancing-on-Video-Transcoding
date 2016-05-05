# Proactive-Load-Balancing-on-Video-Transcoding
This is an python application to implement proactive load balancing using video transcoding as load features</br>

Packages used </br>
1.Python</br>
2.Socket</br>
3.SkLearn</br>
4.Numpy</br>
5.Bluelet</br>

This application is using Support Vector Regression for prediciting the transcoding time

Follow this link for more detail:</br>
1.http://scikit-learn.org/stable/modules/svm.html#svm </br>
2.http://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#example-svm-plot-svm-regression-py </br>
3.https://docs.python.org/2/library/socket.html </br>
4.https://github.com/sampsyo/bluelet </br>



To Implement this </br>
Step 1- Run server1.py server2.py and server3.py pyton file </br>
step 2- Run tough_call.py</br>
Step 3- Run sendfile_client.py</br>

Please read this paper for More informations
http://ieeexplore.ieee.org/xpl/abstractKeywords.jsp?reload=true&arnumber=6890256 </br>

</h3>Implementation Detail </h3>
</p>
We begin with by understanding the client side implementation of the project. The client starts off by collection ten random datasets from the actual dataset that contain around 1 million data points . These collected data points are then encapsulated into an object of class video_request that contains all the parameters that will be required to train our machine learning algorithm. These objects are then forwarded to the load balancer by establishing a connection using python sockets. The load balancer maintains this connection using a multi-threaded environment , that adds the functionality of accepting requests from multiple clients and process them concurrently. After accepting the request from the client , the load balancer send this data for processing by the machine learning algorithm

The machine learning algorithm uses SVR(support vector regression) for predicting the transcoding time for the videos that client is requesting for  to be transcoded .  SVR algorithm first trains data to create a regression function . The kernel involved for generating this function is radical base function. For training the kernel we gathered 1000 random points from the original dataset. These random data points are then converted to an numpy array IE an multi dimension array having values converted to the exponential values. These data points are  then preprocessed using a scalar function. This scalar function converts the data point to values centered around the origin of the axis. The final dataset and the transcoding time for these final dataset is then trained using the rbf function . This function is then fed with data points sent by the client and the output of this function is the transcoding time.

Using this transcoding time, the load balancer allocates the load to the servers having higher available space and time and continues this process until all the load has been completely divided among the servers.
</p>


