#!/usr/bin/python3
from packeter import *
from codec import *
from config import *

class Receiver:
    def receive(self, encodedDataInPackets):
        decoder = Codec()
        packeter = Packeter()
        self.dataAfterDecodingInPackets = []
        self.howManyFailed = 0
        for packet in encodedDataInPackets:
            try:
                self.dataAfterDecodingInPackets.append(decoder.decodePacket(packet))
            except:
                self.dataAfterDecodingInPackets.append(bytearray("\0"*configPacketSize, "UTF-8"))
                self.howManyFailed += 1

        self.data = packeter.unpack(self.dataAfterDecodingInPackets)