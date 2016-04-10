import json, os

home = "/share/"
prefix = "ProjectData/"
with open('defects4j.json') as data_file:    
    data = json.load(data_file)

for proj in data["ProjectNames"]:
	if not os.path.exists(prefix +proj):
		os.makedirs(prefix +proj)
	for i in range(1 , data["Projects"][proj]["NumOfBugs"] + 1):
		path = "/share/output/" + proj + "/" + str(i) + "/" 
		cpy= "cp /share/generate-results.py " + path
		cd= "cd " + path
		execute= "python generate-results.py " + proj + " " + str(i)
		rm= "rm generate-results.py"
		remove_column="cut -d, -f4 --complement result.csv > result.csv"
		print cpy
		print cd
		print execute
		print rm
		print remove_column
