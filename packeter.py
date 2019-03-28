#!/usr/bin/python3
from config import *

class Packeter:

    def __init__(self):
        self.packetSize = configPacketSize

    def setPacketSize(self, size):
        self.packetSize = size

    def pack(self, data):
        dataInPackets = []
        i = self.packetSize
        while i < len(data):
            packet = data[i-self.packetSize:i]
            dataInPackets.append(packet)
            i += self.packetSize
        #appending last packet
        packet = data[i-self.packetSize:]
        dataInPackets.append(packet)
        return dataInPackets

    def unpack(self, dataInPackets):
        data = bytearray()
        for packet in dataInPackets:
            data += packet
        return data