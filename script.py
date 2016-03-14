import json, os
prefix = "ProjectData/"
with open('defects4j.json') as data_file:    
    data = json.load(data_file)
for proj in data["ProjectNames"]:
	if not os.path.exists(prefix +proj):
		os.makedirs(prefix +proj)
	for i in range(1 , data["Projects"][proj]["NumOfBugs"] + 1):
		path = prefix + proj + "/" + str(i)
		if not os.path.exists(path):
			os.makedirs(path)
		open(path+"/data.csv", "a").close()# TODO create a script to calculate data for each bugfix level
