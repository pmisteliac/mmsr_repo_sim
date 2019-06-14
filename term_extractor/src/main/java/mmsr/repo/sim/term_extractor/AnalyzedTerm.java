package mmsr.repo.sim.term_extractor;

public final class AnalyzedTerm {
	
	private final String term;
	private final double frequency;
	
	public AnalyzedTerm(String term, double frequency) {
		this.term = term;
		this.frequency = frequency;
	}
	
	@Override
	public String toString() {
		return term + ";" + frequency;
	}

}
