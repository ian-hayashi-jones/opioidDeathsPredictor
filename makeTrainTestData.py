### makeTrainTestData ###
# 
# Takes as input aggregate county data ("aggregateData201x"aggregateData201x.tsv")
# Outputs to two files: training and testing files
# Format of tsv output files:
# num opioid prescrips (int), num total prescrips (int), 
# % opioid prescrips (float), # total population, % opioid deaths (float)
# "num" version of output file uses # opioid deaths as dependent variable
# instead of % opioid deaths

import sys, random

trainFile = open("trainData2013.tsv", "w")
testFile = open("testData2013.tsv", "w")

for line in sys.stdin:
    data = line.split("\t")

    if data[5] != "0":
        numOpioids = data[4]
        numTotal = data[5]
        percentOpioids = data[6].strip("\n")
        population = data[2]
        percentDeaths = data[3]
        numOpioidDeaths = data[1]

        output = numOpioids + "\t" + numTotal + "\t" + percentOpioids + "\t" \
                + population + "\t" + percentDeaths
        #output = numOpioids + "\t" + numTotal + "\t" + percentOpioids + "\t" \
        #        + population + "\t" + numOpioidDeaths

        # 20% testing data, 80% training data
        if random.randint(0, 9) < 2:
            testFile.write(output) 
            testFile.write("\n")
        else:
            trainFile.write(output)
            trainFile.write("\n")

trainFile.close()
testFile.close()
