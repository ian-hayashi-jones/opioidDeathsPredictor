### error.py ###
# 
# Methods for determining the error of the predictor models
#

import math
import numpy as np



# Prints mean squared error and average percent error
def print_error(predict_Y, true_Y):
    
    # The mean squared error
    MSE = 0.0
    for i in range(len(predict_Y)):
        #print("true_Y[{}] = {}".format(i, true_Y[i]))
        #print("predict_Y[{}] = {}".format(i, predict_Y[i]))
        error = abs(true_Y[i] - predict_Y[i])
        
        MSE += error
        #print("MSE = {}".format(MSE))

    print("MSE: %.2f" % MSE)
    print("RMSE: %.2f" % math.sqrt(MSE))

    # Average percent error
    runningAvgPercentOff = 0.0
    n = len(predict_Y)
    for i in range(n):
        runningAvgPercentOff += abs(1.0 - (predict_Y[i] * 1.0 / true_Y[i])) / n
    runningAvgPercentOff *= 100
    print("Mean percentage off: %.3f" % runningAvgPercentOff + "%")


