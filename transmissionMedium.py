#!/usr/bin/python3
from random import uniform
from random import random
from config import *

class TransmissionMedium:

    def __init__(self):
        self.lower = configMinimumProbability
        self.upper = configMaximumProbability

    def setMinimumProbability(self, minimumProbability):
        self.lower = minimumProbability

    def setMinimumProbability(self, maximumProbability):
        self.upper = maximumProbability

    def transmitPacket(self, data):
        packetLength = len(data)
        dataAfterTransmission = bytearray()
        for byte in data:
            #create bit mask
            mask = 0
            for i in range(8):
                mask << 1
                #probability of error
                currentProbability = uniform(self.lower, self.upper)
                if random() <= currentProbability:
                    mask += 1
            #xoring data with mask changes data onnly if bit in mask is 1
            byteAfterTransmission = byte ^ mask
            dataAfterTransmission.append(byteAfterTransmission)
        return dataAfterTransmission