#########################################################################
# This python script takes Deep Learning Studio's Infered results file i.e., Validation / Test dataset prediction results file
# as input (in CSV format) and output class-wise accuracies (%) on terminal.
#
# The order of column values (in Deep Learning Studio's CSV file) is as given below:
#
# 0 = image id, 1 = actual class label, 2 = predicted calss label, 3 = probability
#
# Author: Dr. Arun Sharma, Senior Information Scientist, DBT Apex, ICGEB, New Delhi, India
#
# Date: 23-09-2019
# Note: This script has been run and tested on Python 2.7.15+ version
#########################################################################


from decimal import *
getcontext().prec = 4

dog_breeds = {'Dingo': 0, 'Dhole': 0, 'Pug': 0, 'Boxer': 0}## Actual Class Labels 
dog_breeds_all = {'Dingo': 0, 'Dhole': 0, 'Pug': 0, 'Boxer': 0}## Actual Class Labels

f = open("result_test.csv", "r")## Deep Learning Studio's Infered results file name
for x in f:
  y = x.rstrip('\r\n')
  z = y.split(',')
#  print z[0] + "\t" + z[1] + "\t" + z[2] + "\t" + z[3]
  act = z[1]
  pred = z[2]
  if act == pred:
     dog_breeds[act] = dog_breeds[act] + 1
     dog_breeds_all[act] = dog_breeds_all[act] + 1
  else:
     dog_breeds_all[act] = dog_breeds_all[act] + 1

#print(dog_breeds)
#print(dog_breeds_all)

print"Dog Breed\tAccuracy(%)"
for k, v in dog_breeds.items():
    #print(k, ":", v)
    tot = dog_breeds_all[k]
    #print(tot)
    acc = Decimal(v)/Decimal(tot)
    #print(acc)
    acc = Decimal(acc * 100)
    print k+'\t',format(acc)
    #print(k, ':', acc, '%')
