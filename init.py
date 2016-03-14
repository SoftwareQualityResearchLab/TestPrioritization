import json, os
with open('defects4j.json') as data_file:    
    data = json.load(data_file)
for proj in data["ProjectNames"]:
	if not os.path.exists(proj):
		os.makedirs(proj)
	for i in range(1 , data["Projects"][proj]["NumOfBugs"] + 1):
		path = proj + "/" + str(i)
		if not os.path.exists(path):
			os.makedirs(path)
		open(path+"/data.csv", "a").close()
