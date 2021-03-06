import csv, os, subprocess, StringIO, numpy, sys

def main():
	ignoreTestList = ["org.apache.commons.math3.random.SynchronizedRandomGeneratorTest#testMath899Sync\n",
	"org.apache.commons.math3.analysis.integration.gauss.BaseRuleFactoryTest#testConcurrentCreation\n"]
	pwd = os.getcwd()
	for number in range(int(sys.argv[1]),int(sys.argv[2])):
		#projectPath = "/share/ProjectData/Math/"+`number`
		#finalResult = "/share/TestPrioritization/test-coverage/result"+"/final_"+`number`+".csv"

		projectPath = "/home/sajad/workspace/commons-math"
		finalResult = "/home/sajad/workspace/commons-math/final.csv"
		
		reportPath = projectPath+"/report.csv"
		jacocoPath = projectPath+"/jacoco.exec"
		
		subprocess.call(makeRemoveJacocoCommand(jacocoPath), shell=True)
		subprocess.call(makeRemoveReportCommand(reportPath), shell=True)

		testFinderCommand = "bash "+pwd+"/TestFinder_release/run_testfinder.sh "+projectPath+" org.apache.commons.math3"
		testMethods = subprocess.check_output(testFinderCommand, shell=True)
		s = StringIO.StringIO(testMethods)
		numberOfAllTest = 0
		numberOfFailedTest = 0
		numberOfRowOfCsvFile = 0

		for test in s:
			indexOfSharp = test.index('#')
			if test in ignoreTestList :
				continue
			if test.endswith("AbstractTest", 0,indexOfSharp):
				continue
			numberOfAllTest+=1
			if numberOfAllTest == 1:
				output = subprocess.check_output(makeJacocoCommand(test, projectPath, pwd), shell=True)
				print output
				output = subprocess.check_output(makeReportBuilderCommand(pwd, projectPath), shell=True)
				print output
				output = subprocess.check_output(makeRemoveJacocoCommand(jacocoPath), shell=True)
				print output
				with open(reportPath, "rb") as f:
					reader=csv.reader(f,delimiter=',')
					x=list(reader)
					tmpResult=numpy.array(x).astype('string')
					numberOfRowOfCsvFile = tmpResult.shape[0]
					output = subprocess.check_output(makeRemoveReportCommand(reportPath), shell=True)
					print output
					
		result = numpy.empty(shape=(numberOfRowOfCsvFile,numberOfAllTest+1), dtype=object)
		print result.shape					
		s = StringIO.StringIO(testMethods)
		i=0
		
		for test in s:
			print "test="+test
			indexOfSharp = test.index('#')
			if test in ignoreTestList :
				continue
			if test.endswith("AbstractTest", 0,indexOfSharp):
				continue
			output = subprocess.check_output(makeJacocoCommand(test, projectPath, pwd), shell=True)
			if output == "true":
				numberOfFailedTest+=1
			output = subprocess.check_output(makeReportBuilderCommand(pwd, projectPath), shell=True)
			print output
			output = subprocess.check_output(makeRemoveJacocoCommand(jacocoPath), shell=True)
			print output
			i+=1
			if i == 1:
				result[0][0]="methodName/testName"
				with open(reportPath) as f:
					readerOfCsv = csv.reader(f, delimiter=',')
					next(readerOfCsv, None)
					j=1
					for row in readerOfCsv:
						result[j][0]=row[0]
						j+=1
			with open(reportPath) as f:
				reader = csv.reader(f, delimiter=',')
				next(reader, None)
				result[0][i]=test[:-1]
				j=1
				for row in reader:
					result[j][i]=row[1]
					j+=1
			output = subprocess.check_output(makeRemoveReportCommand(reportPath), shell=True)
			print output
			print i
			#if i==2:
			#	break
	
	#       print result
		numpy.savetxt(finalResult, result, delimiter=",",  fmt="%s")
		print "number of failed test methods="
		print numberOfFailedTest
		print "total number of test methods="
		print numberOfAllTest


def makeJacocoCommand(testName, projectPath, pwd):
	return "java -javaagent:"+pwd+"/jacoco/lib/jacocoagent.jar=destfile="+projectPath+"/jacoco.exec -cp .:"+pwd+"/runSingleTestWithJunit/classes/:"+projectPath+"/target/classes/:"+projectPath+"/target/test-classes/:/usr/share/java/junit-4.8.2.jar SingleJUnitTestRunner "+testName

def makeReportBuilderCommand(pwd, projectPath):
	return "java -jar "+pwd+"/JacocoReportBuilder_relase/JacocoReportBuilder-1.0.0.jar "+projectPath

def makeRemoveJacocoCommand(jacocoPath):
	return "rm "+jacocoPath

def makeRemoveReportCommand(reportPath):
	return "rm "+reportPath

if __name__ == '__main__':
    main()