#!/usr/bin/python3

from sender import *
from receiver import *
from config import *
from encodingType import *

def test(howManyTimes, whichEncoding, outputFile):
    file = open(outputFile, "w")
    sender = Sender()
    receiver = Receiver()
    #Ustaw kodowanie do testu
    configEncodingType = whichEncoding
    #Wykonaj howManyTimes testów i zapisz wyniki do pliku
    for j in range(howManyTimes):
        receiver.receive(sender.sendData())

        corruptedAfterDecodingCount = 0

        for i in range(len(sender.dataInPackets)):
            if sender.dataInPackets[i] != receiver.dataAfterDecodingInPackets[i]:
                corruptedAfterDecodingCount += 1
        #Jeśli weźmiemy liczbę wszystkich zepsutych pakietów po zdekodowaniu i odejmiemy ilość wykrytych 
        #ale nie naprawionych pakietów to uzyskamy liczbę niewykrytych błędów
        corruptedAndNotDetected = corruptedAfterDecodingCount - receiver.howManyFailed
        #Jeśli weźmiemy liczbę wszystkich pakietów popsutych po przesłaniu i odejmiemy ilość nie naprawionych
        #oraz nie wykrytych błędów to uzyskamy liczbę naprawionych błędów
        corruptedButRepaired = sender.corruptedPacketsCount - receiver.howManyFailed - corruptedAndNotDetected

        file.write(str(sender.correctPacketsCount) + ",")
        file.write(str(corruptedButRepaired) + ",")
        file.write(str(receiver.howManyFailed) + ",")
        file.write(str(corruptedAndNotDetected) + "\n")
    file.close()


test(1000, EncodingType.REED_SOLOMON.value, "output_reed_solomon.csv")
test(1000, EncodingType.BCH.value, "output_BCH.csv")
