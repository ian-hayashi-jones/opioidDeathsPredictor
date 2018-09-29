### filterCTDeaths.py ###
#
# Input: drugdeathsCT.tsv -- drug overdose data for Connecticut 
# Arguments: argv[1] = target date
# Filters through the Connecticut overdose death data
# Output: prints number of deaths in a given year from opioid overdose
#

import sys

firstLine = True
deathCount = 0

targetYear = sys.argv[1]
for line in sys.stdin:
    if firstLine:
        firstLine = False
        continue

    data = line.split("\t")
    date = data[0]
    year = date[-2:]
    age = 0
    if data[3] == "":
        continue
    else:
        age = int(data[3])

    if age >= 65:
        if ("20" + year) == targetYear:
            # Opioids (fentanyl, oxycodone, oxymorphine, 
            # hydrocodone, methadone, tramad, morphine, any)
            if data[16] == 'Y' or data[17] == 'Y' or data[18] == 'Y' or data[20] == 'Y' \
            or data[22] == 'Y' or data[24] == 'Y' or data[25] == 'Y' or data[27]:
                deathCount += 1
print(str(deathCount) + " deaths in Connecticut in " + targetYear + " from opioid overdose.")
    



