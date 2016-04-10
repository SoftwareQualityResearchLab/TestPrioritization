

#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
	script="cp $line /share/file-results/"
	echo $script
	eval $script

done < "$1"
