### filterByState.py ###
#
# Filters out aggregate data for specific states
#

import sys

states = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        states.append(sys.argv[i])

for line in sys.stdin:
    data = line.split("\t")
    state = (data[0])[-2:]
    if state in states:
        print(line.strip())

