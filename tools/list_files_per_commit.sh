cat directories.txt | while read directory; do
	echo $directory
	cd "${directory/output/ProjectData}"
#	ls
	cat $directory"files_name.txt" | while read x; do
        	echo $x >>$directory"commiters_files.txt"
		git log -1 --format="%ae" --name-only $x | wc -l >> $directory"commiters_files.txt"

        	echo $x >>$directory"commits_files.txt"
        	git rev-list --all --count $x  >> $directory"commits_files.txt"
	done
#	pwd
done
