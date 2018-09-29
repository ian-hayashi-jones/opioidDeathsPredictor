### data.py ###
#
# Takes training and testing input files
# Outputs them as lists that are ready for use with sklearn predictors
#
import sys


def getTrainXY():
    train_X = []
    train_Y = []
    with open("TRAIN_DATA/trainData2013.tsv") as f:
        for line in f:
            data = line.split("\t")
            x = []
            x.append(int(data[0]))      # num opioid prescripts
            x.append(int(data[1]))      # num total prescripts
            x.append(float(data[2]))    # % opioid prescripts
            x.append(int(data[3]))      # num total population
            train_X.append(x)
            train_Y.append(float(data[4]))  # num opioid deaths || % opioid deaths
    return (train_X, train_Y)


def getTestXY():
    test_X = []
    test_Y = []
    with open("TEST_DATA/testData2013.tsv") as f:
        for line in f:
            data = line.split("\t")
            x = []
            x.append(int(data[0]))      # num opioid prescripts
            x.append(int(data[1]))      # num total prescripts  
            x.append(float(data[2]))    # % opioid prescripts   
            x.append(int(data[3]))      # num total population
            test_X.append(x)
            test_Y.append(float(data[4]))   # num opioid deaths || % opioid deaths
    return (test_X, test_Y)



train_data = getTrainXY()
train_X = train_data[0]
train_Y = train_data[1]

test_data = getTestXY()
test_X = test_data[0]
test_Y = test_data[1]
