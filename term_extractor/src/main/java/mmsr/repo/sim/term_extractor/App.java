package mmsr.repo.sim.term_extractor;

public class App {
	public static void main(String[] args) {
		Repository repo = new Repository("C:/Temp/git/httputil");
		System.out.println(repo);
		repo.getAllJavaCompilationUnits().stream().forEach(cu -> System.out.println(cu.getTypeNames()));
	}
}
