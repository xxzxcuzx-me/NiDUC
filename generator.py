#!/usr/bin/python3

from os import urandom

class Generator:

    def generateBytes(self, howManyBytes):
        randomBytes = urandom(howManyBytes)
        return randomBytes