#!/usr/bin/python

import sys


maximo = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if thisKey not in maximo.keys():
	maximo[thisKey]=float(thisSale)
    
    else:
	maximo[thisKey]+=float(thisSale)


for key, value in maximo.items():
    print(key+"\t"+str(value))

