package mmsr.repo.sim.term_extractor;

import java.util.Collection;
import java.util.List;

public final class TfIdfCalculator {
	
	private TfIdfCalculator() {
		
	}

	public static double calcTf(List<String> docTerms, String term) {
		double termCount = docTerms.stream().filter(docTerm -> docTerm.equalsIgnoreCase(term)).count();
		return termCount / docTerms.size();
	}

	public static double calcIdf(Collection<JavaCompilationUnit> allJavaCompilationUnits, String term) {
		double n = 0;
		for (JavaCompilationUnit compilationUnit : allJavaCompilationUnits) {
			for (String currentTerm : compilationUnit.getTerms()) {
				if (term.equalsIgnoreCase(currentTerm)) {
					n++;
					break;
				}
			}
		}
		return Math.log(allJavaCompilationUnits.size() / n);
	}

	public static double calcTfIdf(List<String> terms, Collection<JavaCompilationUnit> allJavaCompilationUnits, String term) {
		return calcTf(terms, term) * calcIdf(allJavaCompilationUnits, term);

	}

}
