#!/bin/bash

if [ $# -eq 0 ]; then
	echo "usage: run_testfinder.sh [main-test-package]"
	echo "main-test-package example: org.apache.commons.math3"
	exit
fi

java -cp target/classes:target/test-classes:TestFinder.jar:lib/* org.testfinder.TestFinder $1
