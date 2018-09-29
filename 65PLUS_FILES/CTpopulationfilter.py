### CTpopulationfilter.py ###
#
# Input: CTpop.txt -- population data for Connecticut from years 2012-2017
# Arguments: argv[1] = target year
# Output: Connecticut's 65+ population of a given year
#

import sys


totalpop = 0
firstLine = True
for line in sys.stdin:
    if firstLine:
        firstLine = False
        continue
    data = line.split("\t")
    year = data[5]
    agegrp = int(data[6])
    population = int(data[7])
    
    # 65+ age groups
    if agegrp > 13 and agegrp < 19:
        # year: 6-->2013, 7-->2014, 8-->2015
        targetYear = sys.argv[1] 
        yearCode = 0
        if targetYear == "2013":
            yearCode = "6"
        if targetYear == "2014":
            yearCode = "7"
        if targetYear == "2015":
            yearCode = "8"
        if year == yearCode:
            totalpop += population

if targetYear == "2013" or targetYear == "2014" or targetYear == "2015":
    print("65+ population in CT in year " + targetYear + " = " + str(totalpop))
else:
    print("The given year's data is not available")


