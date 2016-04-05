#!/bin/bash
# time of commit: git show -s --format=%ci 0da657a65c92b086a301a6ffe9e34ec272f8889c
# commit id of last original version: git log --format="%H" -n 4 | tail -n 1
# time of last original version: git show -s --format=%ci `git log --format="%H" -n 4 | tail -n 1`
# list of buggy changes files: defects4j export -p classes.modified
for (( i=1;i<=106;i++)) do
b="b"
buggyVersion="$i$b";
folder="/tmp/$i$b";
defects4j checkout -p $1 -v $buggyVersion -w $folder;
cd $folder;
reportAddress="/home/sajad/workspace/commons-math-reports/$buggyVersion";
mkdir -p $reportAddress;
git show -s --format=%ci `git log --format="%H" -n 4 | tail -n 1` > $reportAddress/time;
defects4j export -p classes.modified > $reportAddress/modifiedClass;
done

