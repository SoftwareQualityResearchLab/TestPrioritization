import csv, os, subprocess, StringIO

pwd = os.getcwd()
projectPath = "/home/sajad/workspace/commons-math"
finalResult = projectPath+"/final.csv"
finalTmpResult = projectPath+"/final_tmp.csv"

#subprocess.check_output("mkdir "+csvReports, shell=True)

testFinderCommand = "bash "+pwd+"/TestFinder_release/run_testfinder.sh "+projectPath+" org.apache.commons.math3"
testMethods = subprocess.check_output(testFinderCommand, shell=True)
s = StringIO.StringIO(testMethods)
numberOfAllTest = 0
numberOfFailedTest = 0

for test in s:
	print "test="+test
	indexOfSharp = test.index('#')
	if test.endswith("AbstractTest", 0,indexOfSharp):
		continue 
	jacocoCommand = "java -javaagent:"+pwd+"/jacoco/lib/jacocoagent.jar=destfile="+projectPath+"/jacoco.exec -cp .:"+pwd+"/runSingleTestWithJunit/classes/:"+projectPath+"/target/classes/:"+projectPath+"/target/test-classes/:/usr/share/java/junit-4.8.2.jar SingleJUnitTestRunner "+test
	output = subprocess.check_output(jacocoCommand, shell=True)
	if output == "true":
		numberOfFailedTest+=1
	numberOfAllTest+=1
	reportBuilderCommand = "java -jar "+pwd+"/JacocoReportBuilder_relase/JacocoReportBuilder-1.0.0.jar "+projectPath
	output = subprocess.check_output(reportBuilderCommand, shell=True)
	print output
	removeJacocoCommand = "rm "+projectPath+"/jacoco.exec"
	output = subprocess.check_output(removeJacocoCommand, shell=True)
	print output
	
	if numberOfAllTest == 1:
		output = subprocess.check_output("mv "+projectPath+"/report.csv "+finalResult, shell=True)
		with open(finalResult, 'rb') as inFile, open(finalTmpResult, 'wb') as outfile:
			r = csv.reader(inFile)
			w = csv.writer(outfile)

			next(r, None)  # skip the first row from the reader, the old header
			# write new header
			w.writerow(['methodName/testName', test[:-1]])

			# copy the rest
			for row in r:
				w.writerow(row)
		
		moveCommand = "mv "+finalTmpResult+" "+finalResult
		output = subprocess.check_output(moveCommand, shell=True)
		print output
		continue
	'''
	with open(projectPath+"/report.csv") as f:
		r = csv.reader(f, delimiter=',')
		next(r, None)
		dict1 = {row[0]: row[1] for row in r}
	'''	
		
	with open(finalResult,'r') as csvinput:
		with open(projectPath+"/report.csv") as f:
			with open(finalTmpResult, 'w') as csvoutput:
				writer = csv.writer(csvoutput, delimiter=',')
				reader = csv.reader(csvinput, delimiter=',')
				r = csv.reader(f, delimiter=',')
				next(r, None)

				all = []
				row0 = next(reader)
				row0.append(test[:-1])
				all.append(row0)

				for row in reader:
					rowAppend = next(r)
					row.append(rowAppend[1])
					all.append(row)

				writer.writerows(all)
		
		
		#dict2 = {row[0]: row[1] for row in r}
	
	'''
	keys = set(dict1.keys() + dict2.keys())
	with open(finalTmpResult, 'wb') as f:
		w = csv.writer(f, delimiter=',')
		w.writerows([[key, dict1.get(key, "''"), dict2.get(key, "''")] for key in keys])
	'''	
	moveCommand = "mv "+finalTmpResult+" "+finalResult
	output = subprocess.check_output(moveCommand, shell=True)
	print output
	

	removeCommand = "rm "+projectPath+"/report.csv "#+csvReports+test[:-1]+".csv"
	output = subprocess.check_output(removeCommand, shell=True)
	print output
		
		

print "number of failed test methods="+numberOfFailedTest
print "total number of test methods="+numberOfAllTest
#khoroji'ha ra bayad check konim ke dorost bashad.
#bayad csv ha ra yeki konim va edameye majera


