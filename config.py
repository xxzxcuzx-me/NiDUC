#transmissionMedium
#range of probability of corruption of single bit
configMinimumProbability = 0.001
configMaximumProbability = 0.002

#sender
configDataType = 2
#size of data to send if chosen random data
configDataSize = 10000
#name of the file with data to send if chosen data from file
configFileName = "data.txt"

#packeter
configPacketSize = 30

#encoder
configEncodingType = 1
configReedSolomonRedundantBytes = 3
#BCH
configBCHPolynomial = 8219
configBCHBits = 200
#BCH tends to crash if packet size and BCHBits are set inappropriately