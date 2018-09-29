### makeTrainTest.py ###
# 
#
#
#

import sys


firstLine = True
for line in sys.stdin:
    if firstLine:
        firstLine = False
        continue
    data = line.split(",")

    output = ""
    for i in range(5, len(data)):
        x = data[i].strip()
        if i == 13:
            x = x.strip("\"")
        output += x
        
        if i < len(data) - 1:
            output += "\t"

    print(output)

   
