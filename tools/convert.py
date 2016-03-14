import csv
import re
main_list = []
# pattern = re.compile("^([A-Z][0-9]+)*$")
pattern = re.compile("[0-9]*\/[0-9]*")
data = []
with open("output.csv", 'rU') as f:  #opens PW file
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

    for idx,row in enumerate(data):
        for idy,item in enumerate(row):
        	if pattern.match(item):
        		try:
        			print item
        			data[idx][idy] =  eval(item)
        		except ZeroDivisionError:
        			print("boooogh")
        			data[idx][idy] =  0
        		except SyntaxError:
        			data[idx][idy] = 0

with open("output2.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(data)