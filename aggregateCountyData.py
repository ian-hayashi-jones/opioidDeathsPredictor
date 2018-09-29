### aggregateCountyData.py ###
# 
# Creates a dictionary from zipcodes to county, state
# Then uses this dictionary to match zipcode data from the filtered prescriber data
# to the opioid overdose data
# Outputs this data in the following tsv form:
# (sorted alphabetically by state name)
# county, num deaths by opioids, population, % death by opioids (% of total pop.)
# num opioid prescripts, num total prescripts, % opioid prescripts (% of total prescripts)

import sys


"""
Create Zipcode to County, State dictionary
"""
def createCodeToNameDict():
    codeToNameDict = {}
    ## Populate dictionary with 
    # key: (state code, county code)
    # val: (county name, state name)
    with open("counties.csv") as f:
        for line in f:
            data = line.split(",")
            stateCode = data[1]
            countyCode = data[2]
            stateName = data[0]
            countyName = data[3]
            key = (stateCode, countyCode)
            val = (countyName, stateName)
            codeToNameDict[key] = val 

    zipcodeToCountyDict = {}
    ## Populate dictionary with
    # key: (zipcode)
    # val: (county name, state name)
    with open("zipcodes.csv") as f:
        for line in f:
            data = line.split(",")
            zipcode = data[0]
            stateCode = data[1]
            countyCode = data[2]
            key = (stateCode, countyCode)
            countyState = codeToNameDict[key]
            countyName = countyState[0]
            stateName = countyState[1]

            val = countyName + ", " + stateName
            zipcodeToCountyDict[zipcode] = val
    return zipcodeToCountyDict


"""
Match zipcodes to counties and output county aggregate data
"""
def createCountyDataDict(zipcodeToCountyDict):
    # County data dictionary for output
    # Key = county
    # Value = [numDeaths, population, opioidDeathRatio,# opioid prescripts, # total prescripts]
    countyDataDict = {}
    ## Populate county data dictionary with death data
    with open("deaths2013.tsv") as f:
        for line in f:
            data = line.split("\t")
            county = data[0]
            numDeaths = int(data[1])
            population = int(data[2])
            opioidDeathRatio = 1.0 * numDeaths / population # opioid deaths as % of total population

            # Add county as key in countyDict
            if county not in countyDataDict.keys():
                countyDataDict[county] = [numDeaths, population, opioidDeathRatio, 0, 0]

    ## Populate county data dictionary with prescriber data, matching zipcodes to counties
    with open("filteredprescriberdata2013.tsv") as f:
        for line in f:
            data = line.split("\t")
            zipcode = data[0]
            numOpioids = int(data[1])
            numTotal = int(data[2])

            # Add zipcode data to the correct county
            if zipcode in zipcodeToCountyDict.keys():
                county = zipcodeToCountyDict[zipcode]
                if county in countyDataDict.keys():
                    countyDataDict[county][3] = numOpioids
                    countyDataDict[county][4] = numTotal
    return countyDataDict


"""
Outputs the data in alphabetical order by state
"""
def outputData(countyDataDict):
    # Sort data alphabetically by state
    outputDict = {}
    for key in countyDataDict.keys():
        countyName = key[:-4]
        stateName = key[-2:]
        newKey = (stateName, countyName)
        outputDict[newKey] = countyDataDict[key]

    # Output data
    for key in sorted(outputDict.keys()):
        countyData = outputDict[key]
        countyName = key[1]
        stateName = key[0]
        output = countyName + ", " + stateName + "\t"
        for elem in countyData:
           output += str(elem) + "\t"
        if int(countyData[4]) == 0:     # If total population is 0
            output += "0"
        else:
            output += str(1.0 * int(countyData[3]) / int(countyData[4]))
        print output



"""
MAIN
"""
zipcodeToCountyDict = createCodeToNameDict()
countyDataDict = createCountyDataDict(zipcodeToCountyDict)
outputData(countyDataDict)



