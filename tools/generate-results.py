import csv
import sys
#print(sys.argv)
proj = sys.argv[1]
version = sys.argv[2]
bugFile = list(csv.reader(open(proj+version+"-File.csv")))

#print bugFile[3][2]
#print bugFile[0]
package_names_list = list(csv.reader(open("package_names.txt", 'rU'), delimiter=";",dialect=csv.excel_tab))
names_dictionary={}
#print package_names_list[0]
for i in range(0, len(package_names_list)):
	names_dictionary[package_names_list[i][0]] = package_names_list[i]
#print names_dictionary[package_names_list[0][0]]
commiters = tuple(open("commiters_files.txt", 'r'))
for i in range(0 , len(commiters)/2):
	names_dictionary[commiters[2*i].rstrip()].append(commiters[2*i+1].rstrip())
#print names_dictionary[package_names_list[0][0]]
commits = tuple(open("commits_files.txt", 'r'))
for i in range(0 , len(commits)/2):
	names_dictionary[commits[2*i].rstrip()].append(commits[2*i+1].rstrip())
#print names_dictionary[package_names_list[0][0]]

bugFile[0].append("commiters")
bugFile[0].append("commits")
bugFile[0].append("is_buggy")
bugFile[0].append("before_bugs")
bugFile[0].append("after_bugs")
bugs = tuple(open(proj+version+".txt", 'r'))
before_bugs =filter(None, map(str.strip, tuple(open("before_bugs.txt", 'r'))))
after_bugs =filter(None, map(str.strip,tuple(open("after_bugs.txt", 'r'))))

#print bugFile[2][2]

#print bugs
for i in range(1, len(bugFile)):
	bugFile[i][2]=bugFile[i][2].replace("/share/ProjectData/"+ proj + "/" + version + "/", "")
	if len(names_dictionary[bugFile[i][2]]) != 5:
		continue
	bugFile[i].append(names_dictionary[bugFile[i][2]][3])
	bugFile[i].append(names_dictionary[bugFile[i][2]][4])
	bugFile[i][0] = names_dictionary[bugFile[i][2]][1]
	bugFile[i][1] = names_dictionary[bugFile[i][2]][2]
	bugFile[i][4] = str(bugFile[i][4]) + ".00"
	bugFile[i][5] = str(bugFile[i][4]) + ".00"
	bugFile[i][6] = str(bugFile[i][4]) + ".00"
	bugFile[i][7] = str(bugFile[i][4]) + ".00"
	bugFile[i][8] = str(bugFile[i][4]) + ".00"
	bugFile[i][9] = str(bugFile[i][4]) + ".00"
	
	if names_dictionary[bugFile[i][2]][2] in bugs:
		bugFile[i].append(1)
	else:
		bugFile[i].append(0)
	bugFile[i].append(before_bugs.count(names_dictionary[bugFile[i][2]][2]))
	bugFile[i].append(after_bugs.count(names_dictionary[bugFile[i][2]][2]))
	#print before_bugs.count(names_dictionary[bugFile[i][2]][2])
	#print names_dictionary[bugFile[i][2]][2] in before_bugs
		

fl = open('result.csv', 'w')

writer = csv.writer(fl)
for values in bugFile:
    writer.writerow(values)

fl.close()    
