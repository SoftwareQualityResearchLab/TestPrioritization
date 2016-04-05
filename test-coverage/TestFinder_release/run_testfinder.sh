#!/bin/bash

if [ $# -le 1 ]; then
	echo "usage: run_testfinder.sh [absolute-project-path] [main-test-package]"
	echo "main-test-package example: org.apache.commons.math3"
	exit
fi

java -cp $1/target/classes:$1/target/test-classes:TestFinder.jar:lib/* org.testfinder.TestFinder $2
