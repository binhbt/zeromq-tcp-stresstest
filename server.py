import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    #  Wait for next request from client
    socket.send_string("Mesage from 192.168.1.27:5556")
    time.sleep(1)
