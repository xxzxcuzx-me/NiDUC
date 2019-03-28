#!/usr/bin/python3

from sender import *
from receiver import *
import time

sender = Sender()
receiver = Receiver()

startTime = time.time_ns()
receiver.receive(sender.sendData())
endTime = time.time_ns()

assert sender.data == receiver.data
elapsed = endTime - startTime

print("Successful transfer")
print("It took", elapsed, " nanoseconds")