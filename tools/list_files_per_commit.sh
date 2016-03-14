git ls-files *.java > ../file_names.txt

cat ../file_names.txt | while read x ; do	
	git log -1 --format="%ae" --name-only $x | wc -l >> ../commiters_files.txt
	echo "" >> ../commiters_files.txt
	echo $x >>../commiters_files.txt

	git rev-list --all --count $x  >> ../commits_files.txt
	echo "" >> ../commits_files.txt
	echo $x >>../commits_files.txt

done


