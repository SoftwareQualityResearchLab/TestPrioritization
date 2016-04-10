

#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo $line
    eval $line
done < "$1"
