package org.testfinder;

import java.lang.reflect.Method;
import java.util.Set;

import org.reflections.Reflections;
import org.reflections.scanners.MethodAnnotationsScanner;
import org.reflections.util.ClasspathHelper;
import org.reflections.util.ConfigurationBuilder;

public class TestFinder {
	public static void main(String[] args) {
		if (args.length < 1) {
			System.out.println("usage: java -jar TestFinder.jar [package]");
			return;
		}
		Reflections reflections = new Reflections( 
				new ConfigurationBuilder().setUrls( 
						ClasspathHelper.forPackage( args[0] ) ).setScanners(
								new MethodAnnotationsScanner() ) );
		
		Set<Method> methods = reflections.getMethodsAnnotatedWith(org.junit.Test.class);
		for (Method method: methods) {
			System.out.println(method.getDeclaringClass().getCanonicalName()+"#"+method.getName());
		}
	}
}
