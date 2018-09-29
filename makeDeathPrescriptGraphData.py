### makeDeathPrescriptGraphData.py ###
#
#
#

import sys, graph

X = []
Y = []
for line in sys.stdin:
    data = line.split("\t")

    if data[5] != "0":

        percentOpioids = data[6].strip("\n")
        percentDeaths = data[3]
        
        X.append(percentOpioids)
        Y.append(percentDeaths)


for i in range(0, len(X)):
    print("i = " + str(i) + "\t" + X[i] + "\t" + Y[i])

graph.standard_plot(X, Y)



