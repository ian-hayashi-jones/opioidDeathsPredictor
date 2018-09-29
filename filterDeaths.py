### filterDeaths.py ###
# Streams through the opioid mortality data, filtering for given year's data
# Outputs the county, opioid deaths, population in tsv format
#

import sys

for line in sys.stdin:
    data = line.split("\t")

    county = data[1].strip("\"")
    year = data[3].strip("\"")
    deaths = data[5]
    population = data[6]

    if year == "2013":
        print county + "\t" + str(deaths) + "\t" + str(population)

