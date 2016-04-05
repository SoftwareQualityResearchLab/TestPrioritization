#!/bin/bash
while read className
do
	tmp="src/main/java/$className";
	tmp=$(echo $tmp | tr . / );
	tmp="$tmp.java";
	echo $tmp >> normalizedModifiedClasses;
done < allModifiedClass
