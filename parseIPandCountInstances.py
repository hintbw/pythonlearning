
file = open("filepath")
for line in file:
  lineElements = line.split(" ")
  if lineElements[0] in ipAddresses:
    ipAddresses[lineElements[0]] += 1
  else:
    ipaddresses[lineElements[0]] = 1
import operator
sorted_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
list(sorted_dict.keys())[-1]

Take that value and then output to a file and it asked us to use sha1sum of the file to validate it.