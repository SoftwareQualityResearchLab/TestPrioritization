import csv

main_list = []
with open("Test.csv", 'rU') as f:  #opens PW file
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

    for row in data:
        main_list.append(row[3:])
        

        

files = tuple(open("file_names.txt", 'r'))

files_commits = tuple(open("commits_files.txt", 'r'))
f_c=[]
for f in files_commits:
	if not f.isspace():
		f_c.append(f.strip())

files_commiters = tuple(open("commiters_files.txt", 'r'))

f_cr=[]
for f in files_commiters:
	if not f.isspace():
		f_cr.append(f.strip())

main_list[0].append("commit_count")
main_list[0].append("commiter_count")


for f in main_list[1:]:
	i = f_c.index(f[0])
	j = f_cr.index(f[0])
	f.append(f_c[i-1] )
	f.append(f_cr[j-1] )


with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(main_list)