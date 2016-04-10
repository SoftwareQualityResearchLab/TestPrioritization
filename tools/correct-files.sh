#!/bin/bash
for filename in /share/file-results/*.csv; do
	var="cut -d, -f1,2,4 --complement $filename"
	#eval $var >> "${filename/.csv/final.csv}"
	eval $var > "${filename/-File.csv/.csv}"
done
