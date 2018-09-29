### filterOpioids.py ###
# Streams through the prescriber data of a given year
# Outputs zipcode, # opioid prescriptions, # total prescriptions, % opioid prescriptions
#

import sys

# Dictionary of zipcode to [number opioid prescriptions, number total drug prescriptions]
zipToOpiodDict = {} 
firstLine = True
for line in sys.stdin:
    # Skip first line (header)
    if firstLine:
        firstLine = False
        continue

    data = line.split("\t")
    zipcode = data[10]
    
    numOpioids = 0
    if data[50].isdigit():
        numOpioids = int(data[50])
   
    numTotalDrugs = numOpioids
    if data[17].isdigit():
        numTotalDrugs = int(data[17])
    
    if zipcode in zipToOpiodDict.keys():
        zipToOpiodDict[zipcode][0] += numOpioids
        zipToOpiodDict[zipcode][1] += numTotalDrugs
    else:
        zipToOpiodDict[zipcode] = [numOpioids, numTotalDrugs]

for zipcode in zipToOpiodDict.keys():
    numOpioids = zipToOpiodDict[zipcode][0]
    numTotalDrugs = zipToOpiodDict[zipcode][1]
    if numTotalDrugs != 0:
        opioidRate = (1.0 * numOpioids) / numTotalDrugs
        print zipcode + "\t" + str(numOpioids) + "\t" + str(numTotalDrugs) + "\t" + str(opioidRate)

