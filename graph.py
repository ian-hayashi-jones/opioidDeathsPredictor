### graph.py ###
#
#


import matplotlib.pyplot as plt



def standard_plot(X, Y):
   
    plt.title("Opioid Prescription Rates as a factor in Opioid Overdose Rates")
    plt.xlabel("% Opioid Prescriptions")
    plt.ylabel("% Opioid Overdose Deaths")
    plt.plot(X, Y, 'bo')
    plt.axis()
    plt.show()
