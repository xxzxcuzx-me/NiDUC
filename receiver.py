#!/usr/bin/python3
from packeter import *
from codec import *

class Receiver:
    def receive(self, dataInPackets):
        decoder = Codec()
        packeter = Packeter()
        dataAfterDecoding = []
        for packet in dataInPackets:
            dataAfterDecoding.append(decoder.decodePacket(packet))

        self.data = packeter.unpack(dataAfterDecoding)