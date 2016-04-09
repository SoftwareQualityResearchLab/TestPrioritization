#/bin/sh
java -javaagent:/home/sajad/workspace/TestPrioritization/test-coverage/jacoco/lib/jacocoagent.jar=destfile=jacoco.exe -cp .:/home/sajad/workspace/TestPrioritization/test-coverage/runSingleTestWithJunit/classes/:target/classes/:target/test-classes/:/usr/share/java/junit-4.8.2.jar SingleJUnitTestRunner org.apache.commons.math3.fitting.HarmonicFitterTest#testNoError
