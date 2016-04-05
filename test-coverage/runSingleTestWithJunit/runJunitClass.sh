#/bin/sh
java -cp .:target/classes/:target/test-classes/:/usr/share/java/junit-4.8.2.jar org.junit.runner.JUnitCore org.apache.commons.math3.fitting.HarmonicFitterTest;
