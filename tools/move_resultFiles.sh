cat directories.txt | while read directory; do
	echo $directory
	#cd "${directory/output/ProjectData}"
	#rm -f $directory"package_names.txt"
	project=$(echo $directory| cut -d'/' -f 4)
	version=$(echo $directory| cut -d'/' -f 5)
	file_address=$(cat "/share/csv_file_names.txt" | grep "$project$version-File.csv")
	cp $file_address $directory
done
