### filterPrescriptByState.py ###
#
# Input: prescriptsbystate201x.txt -- Medicare prescription data by state
# Arguments: argv[1...] = state abbreviations
# Filters for the target state(s) inputted from the command line
# Output: state, the number of opioid claims, total claims, and rate of opioid claims
# 

import sys

targetStates = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        targetStates.append(sys.argv[i])

firstLine = True
for line in sys.stdin:
    if firstLine:
        firstLine = False
        continue
    data = line.replace('"', '').split("\t")
    state = data[0]
    numOpioidClaims = data[3]
    numTotalClaims = data[5]
    rateOpioidClaims = data[6]

    if state in targetStates:
        print(state + " " + numOpioidClaims + " " + numTotalClaims + " " + rateOpioidClaims)


