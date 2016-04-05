#!/bin/bash
#training data from 40 to 106
for (( i=40;i<=106;i++ )) do
buggyVersion="$i"b;
reportAddress="/home/sajad/workspace/test-pri/commons-math-reports/$buggyVersion";
cat $reportAddress/modifiedClass >> allModifiedClass
echo "" >> allModifiedClass
done
