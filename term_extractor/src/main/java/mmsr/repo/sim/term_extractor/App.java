package mmsr.repo.sim.term_extractor;

public class App {
	public static void main(String[] args) {
		Repository repo = new Repository("C:/Temp/git/httputil");
		System.out.println(repo);
		System.out.println(repo.getAllJavaFilePaths());
	}
}
