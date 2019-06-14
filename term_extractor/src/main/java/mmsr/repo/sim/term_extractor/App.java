package mmsr.repo.sim.term_extractor;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;

public class App {
	public static void main(String[] args) {
		Repository repo = new Repository("C:/Temp/git/httputil");
		System.out.println(repo);
		Collection<JavaCompilationUnit> allJavaCompilationUnits = repo.getAllJavaCompilationUnits();
		allJavaCompilationUnits.stream().forEach(cu -> System.out.println(cu.getTerms()));
		Set<String> allTerms = repo.getAllTerms();

		List<AnalyzedTerm> terms = new ArrayList<>();
		for (JavaCompilationUnit document : allJavaCompilationUnits) {
			for (String term : allTerms) {
				double tfIdf = TfIdfCalculator.calcTfIdf(document.getTerms(), allJavaCompilationUnits, term);
				terms.add(new AnalyzedTerm(term, tfIdf));
			}
		}
		
		System.out.println(terms);
	}
}
