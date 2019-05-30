# zeromq-tcp-stresstest
#Install ZeroMQ lib
pip install pyzmq
#Run client open TCP listen to server with 300 connections
python stress_test.py 300 1000
