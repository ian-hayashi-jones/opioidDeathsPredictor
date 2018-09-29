### multinom_data.py ###
#
# Takes training and testing input files (MULTINOM_PREDICT data)
# Outputs them as lists that are ready for use with sklearn predictors
#

import sys

def getTrainXY():
    train_X = []
    train_Y = []
    with open("MULTINOM_PREDICT/updatedtrain.tsv") as f:
        for line in f:
            data = line.split("\t")
            x = [float(d) for d in data]
            train_X.append(x[:-1])
            train_Y.append(int(x[len(x) - 1]))
    return (train_X, train_Y)

def getTestXY():
    test_X = []
    test_Y = []
    with open("MULTINOM_PREDICT/test.tsv") as f:
        for line in f:
            data = line.split("\t")
            x = [float(d) for d in data]
            test_X.append(x[:-1])
            test_Y.append(x[len(x) - 1])
        return (test_X, test_Y)


train_data = getTrainXY()
train_X = train_data[0]
train_Y = train_data[1]

test_data = getTestXY()
test_X = test_data[0]
test_Y = test_data[1]




