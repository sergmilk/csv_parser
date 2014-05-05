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

import csv

import sys

import re


from collections import defaultdict


col_name = sys.argv[1]
reg = sys.argv[2]

#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader,
    compare a col_name row values and regular expression
    if match we output values sorted by the number of matches
    """

    d = defaultdict(int)   #dictionary with matched values and number of matches

    prog = re.compile(reg) #compiled regular expression from second command line parameter

    reader = csv.DictReader(file_obj, delimiter=',')


    #choose lines that match regular expression and add values to d dictionary
    for line in reader:
        result = prog.match(line[col_name])
        if result is not None :
            d[line[col_name]] += 1


    #Sorted dictionary d output
    for key in sorted(d.keys(),reverse = True):
        print( str(key) + " " + str(d[key]))

#----------------------------------------------------------------------



with open("some.csv") as f_obj:
    csv_dict_reader(f_obj)










