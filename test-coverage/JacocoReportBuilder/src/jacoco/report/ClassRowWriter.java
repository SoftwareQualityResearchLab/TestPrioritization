/*******************************************************************************
 * Copyright (c) 2009, 2016 Mountainminds GmbH & Co. KG and Contributors
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 * 
 * Contributors:
 *    Brock Janiczak - initial API and implementation
 * 
 *******************************************************************************/
package jacoco.report;

import java.io.IOException;

import org.jacoco.core.analysis.IClassCoverage;
import org.jacoco.core.analysis.ICoverageNode.CounterEntity;
import org.jacoco.core.analysis.IMethodCoverage;
import org.jacoco.report.ILanguageNames;

/**
 * Writer for rows in the CVS report representing the summary data of a single
 * class.
 */
public class ClassRowWriter {

//	private static final CounterEntity[] COUNTERS = { CounterEntity.INSTRUCTION,
//			CounterEntity.BRANCH, CounterEntity.LINE,
//			CounterEntity.COMPLEXITY, CounterEntity.METHOD };

	private final DelimitedWriter writer;

	private final ILanguageNames languageNames;

	/**
	 * Creates a new row writer that writes class information to the given CSV
	 * writer.
	 * 
	 * @param writer
	 *            writer for csv output
	 * @param languageNames
	 *            converter for Java identifiers
	 * @throws IOException
	 *             in case of problems with the writer
	 */
	public ClassRowWriter(final DelimitedWriter writer,
			final ILanguageNames languageNames) throws IOException {
		this.writer = writer;
		this.languageNames = languageNames;
		writeHeader();
	}

	private void writeHeader() throws IOException {
		writer.write("methodName", "coverage");
//		for (final CounterEntity entity : COUNTERS) {
//			writer.write(entity.name() + "_MISSED");
//			writer.write(entity.name() + "_COVERED");
//		}
		writer.nextLine();
	}

	/**
	 * Writes the class summary information as a row.
	 * 
	 * @param groupName
	 *            name of the group
	 * @param packageName
	 *            vm name of the package
	 * @param node
	 *            class coverage data
	 * @throws IOException
	 *             in case of problems with the writer
	 */
	public void writeRow(final String packageName, final IClassCoverage c
			,IMethodCoverage m) throws IOException {
		final String className = languageNames.getClassName(c.getName(),
				c.getSignature(), c.getSuperName(),
				c.getInterfaceNames());
		final String methodName = languageNames.getMethodName(className, m.getName(), m.getDesc(), m.getSignature());
	
		if (className.endsWith("{...}") || methodName.endsWith("{...}") || m.getName().equals("<init>"))
			return ;//ignore static and constructor methods
		
		final String fullMethodName = languageNames.getPackageName(packageName)+"."+className+"#"+m.getName();
		writer.write(fullMethodName);

		Double percent = m.getCounter(CounterEntity.INSTRUCTION).getCoveredRatio();
		writer.write(percent.toString());
//		for (final CounterEntity entity : COUNTERS) {
//			final ICounter counter = m.getCounter(entity);
//			writer.write(counter.getMissedCount());
//			writer.write(counter.getCoveredCount());
//		}

		writer.nextLine();
	}

}
