#!/usr/bin/python3
from generator import *
from transmissionMedium import *
from config import *
from packeter import *
from dataType import *
from codec import *

class Sender:
    

    def __init__(self):
        self.dataType = configDataType
        self.dataSize = configDataSize
        self.fileName = configFileName

    def setDataType(self, dataType):
        self.dataType = dataType

    def setDataSize(self, size):
        self.dataSize = size

    def setFileName(self, fileName):
        self.fileName = fileName

    def sendData(self):
        generator = Generator()
        packeter = Packeter()
        encoder = Codec()
        medium = TransmissionMedium()
        self.data = bytearray()
        #generate or load data
        if self.dataType == DataType.RANDOM.value:
            self.data = generator.generateBytes(self.dataSize)
        elif self.dataType == DataType.FILE.value:
            file = open(self.fileName, "rb")
            self.data = file.read()
            file.close()

        self.dataInPackets = packeter.pack(self.data)
        dataInPacketsAfterEncoding = []

        for packet in self.dataInPackets:
            dataInPacketsAfterEncoding.append(encoder.encodePacket(packet))

        dataAfterTransmission = []
        for packet in dataInPacketsAfterEncoding:
            dataAfterTransmission.append(medium.transmitPacket(packet))

        self.corruptedPacketsCount = 0
        for i in range(len(dataInPacketsAfterEncoding)):
            if dataInPacketsAfterEncoding[i] != dataAfterTransmission[i]:
                self.corruptedPacketsCount += 1
        self.correctPacketsCount = len(dataInPacketsAfterEncoding) - self.corruptedPacketsCount
        
        return dataAfterTransmission