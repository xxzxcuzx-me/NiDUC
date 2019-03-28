#!/usr/bin/python3

import reedsolo
import bchlib
from encodingType import *
from config import *

class Codec:

    def __init__(self):
        self.encodingType = configEncodingType

    def encodePacket(self, packet):
        if self.encodingType == EncodingType.REED_SOLOMON.value:
            return reedsolo.RSCodec(configReedSolomonRedundantBytes).encode(packet)
        elif self.encodingType == EncodingType.BCH.value:
            return self.encodeBCH(packet)

    def decodePacket(self, packet):
        if self.encodingType == EncodingType.REED_SOLOMON.value:
            return reedsolo.RSCodec(configReedSolomonRedundantBytes).decode(packet)
        elif self.encodingType == EncodingType.BCH.value:
            return self.decodeBCH(packet)

    def encodeBCH(self, data):
        bch = bchlib.BCH(configBCHPolynomial, configBCHBits)
        ecc = bch.encode(data)
        packet = data + ecc
        return packet

    def decodeBCH(self, packet):
        bch = bchlib.BCH(configBCHPolynomial, configBCHBits)
        data, ecc = packet[:-bch.ecc_bytes], packet[-bch.ecc_bytes:]
        
        try:
            bitflips, corrected, ecc = bch.decode(data, ecc)
        except:
            print("Error during decoding!")
            return bytearray()
        return corrected