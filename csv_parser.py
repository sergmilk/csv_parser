""" Need to create a python script that will open a csv file
   and with a certain column compare values on each row, if
   this value fits a regular expression - should add it to output,
   also output must contain the number of values of each type and
   values should be sorted by the number


some.csv content:

A,B

1,aaac

2,aaab

3,aaac

4,xxx



Run with command line parameters: B aaa



Output:

aaac 2

aaab 1


"""

__author__ = 'User'

import csv

import sys

import re

import collections

from collections import defaultdict


#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    d = defaultdict(int)


    prog = re.compile(sys.argv[2])

    reader = csv.DictReader(file_obj, delimiter=',')



    for line in reader:
        #print(line["sys.argv[1]"])
        result = prog.match(line[sys.argv[1]])
        if result is not None :
            print(line)
            d[line[sys.argv[1]]] += 1

        #if prog.match(line[sys.argv[1]]): print(line)

    #print( list(d.items()))
    print('\ndictionary:')
    print( d )


    print('\nunsorted:')
    for line in d:
        print(line + " " + str(d[line]))

    print('\nsorted:')
    for key in sorted(d.keys(),reverse = True):
        print( str(key) + " " + str(d[key]))



#----------------------------------------------------------------------

#if __name__ == "__main__":

with open("some.csv") as f_obj:
    csv_dict_reader(f_obj)


print("\n--------------\ncommandline parameters:")
print(sys.argv[1] + " " + sys.argv[2])










