import zmq
import sys
host = 'localhost'
port = 5556
subcribe =''
if(len(sys.argv) >4):
   subcribe = sys.argv[4]
if(len(sys.argv) >3):
   port = int(sys.argv[3])
if(len(sys.argv) >2):
   host = sys.argv[2]
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://"+host+":"+str(port))

socket.setsockopt_string(zmq.SUBSCRIBE, subcribe)

while True:
    string = socket.recv_string()
    print(string+"---"+sys.argv[1])
