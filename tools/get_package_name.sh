cat directories.txt | while read directory; do
	echo $directory
	cd "${directory/output/ProjectData}"
	rm -f $directory"package_names.txt"

	cat $directory"files_name.txt" | while read x; do
        	package=$(cat $x | grep -m 1 package | cut -d';' -f 1 | sed 's/package//' | sed -e 's/ *//')
		class=$(echo $x | rev | cut -d'/' -f 1| rev)
		withoutJava=$(echo $class | cut -d'.' -f 1)
		echo "$x;$package.$class;$package.$withoutJava" >> $directory"package_names.txt"
	done
done
