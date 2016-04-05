#/bin/sh
java -cp .:target/classes/:target/test-classes/:/usr/share/java/junit-4.8.2.jar org.junit.runner.JUnitCore org.apache.commons.math3.fitting.HarmonicFitterTest;

java -cp .:/home/sajad/workspace/test-pri/junit/classes/:target/classes/:target/test-classes/:/usr/share/java/junit-4.8.2.jar SingleJUnitTestRunner org.apache.commons.math3.fitting.HarmonicFitterTest#testNoError





java -javaagent:/home/sajad/workspace/test-pri/jacoco/lib/jacocoagent.jar=destfile=jacoco.exec -cp .:/home/sajad/workspace/test-pri/junit/classes/:target/classes/:target/test-classes/:/usr/share/java/junit-4.8.2.jar SingleJUnitTestRunner org.apache.commons.math3.fitting.HarmonicFitterTest#testNoError
