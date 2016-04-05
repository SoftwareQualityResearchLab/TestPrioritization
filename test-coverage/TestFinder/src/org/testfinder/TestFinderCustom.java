package org.testfinder;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;
import java.util.Set;

import org.reflections.Reflections;
import org.reflections.scanners.SubTypesScanner;

public class TestFinderCustom {
	public static void main(String[] args) {
		 Reflections reflections = new Reflections("org.testfinder.test", new SubTypesScanner(false));

		 Set<Class<? extends Object>> allClasses = 
		     reflections.getSubTypesOf(Object.class);
		 
		 for (Class cl: allClasses) {
			 for (Method method: cl.getMethods()) {
				 for (Annotation annotation: method.getAnnotations()) {
					 String name = annotation.annotationType().getName();
					 if (name.equals("org.junit.Test"))
						 break;
				 }
			 }
		 }
	}
}
