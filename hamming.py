def hammdist(s1,s2):
  count = 0
  if len(s1) != len(s2):
    print "string sizes are not equal"
  else:
    for x in range(len(s1)):
      if s1[x] != s2[x]:
        count = count + 1
    return count
outputfile = open("output.txt","w")
freqfile = open("hammfrequency.txt","w")
bitarray = []
f1 = open("bitstring.txt","r")
for x in range(500):
  bitarray.append(f1.readline().strip())
f1.close()
#print bitarray
total = 0
totalmeanhamm = 0
frequency = [0]*5093
for y in range(499):
#  outputfile.write("this is a hamming distance from %d to all other bitstrings \n" %y)
  for z in range(y+1,500):
     hammdistance = hammdist(str(bitarray[y]),str(bitarray[z]))
     mean = 2546.41139078
     totalmeanhamm = totalmeanhamm + (hammdistance - mean)**2
     outputfile.write(str(hammdistance) + "\n")
     total = total + hammdistance
     frequency[hammdistance] = frequency[hammdistance] + 1
outputfile.close()
meanhamm = total/124750.00
standard_deviation = (totalmeanhamm/124750.00)**(0.5)
for index,item in enumerate(frequency):
  if (item > 0):
    freqfile.write("%d\n" %index)
for index,item in enumerate(frequency):
  if (item > 0):
    freqfile.write("%d\n" %item)    
freqfile.close()

