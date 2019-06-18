package mmsr.repo.sim.term_extractor;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class App {
	public static void main(String[] args) {
		List<Repository> repositories = getRepositories();
		List<String> repoCsvRows = new ArrayList<>();
		for (Repository repo : repositories) {
			repoCsvRows.add(repo.getCsvRepresentation());
		}
		try {
			writeOutputFile("result/repos.csv", repoCsvRows);
		} catch (IOException e) {
			e.printStackTrace();
		}
//		Collection<JavaCompilationUnit> allJavaCompilationUnits = repo.getAllJavaCompilationUnits();
//		allJavaCompilationUnits.stream().forEach(cu -> System.out.println(cu.getImportNames()));
	}

	public static List<Repository> getRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.addAll(getHttpRepositories());
		repositories.addAll(getTicTacToeRepositories());
		return repositories;
	}
	
	public static List<Repository> getHttpRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(new Repository("C:/Temp/git/httputil"));
		repositories.add(new Repository("C:/Temp/git/http-client"));
		repositories.add(new Repository("C:/Temp/git/async-http-client"));
		repositories.add(new Repository("C:/Temp/git/http-request"));
		repositories.add(new Repository("C:/Temp/git/okhttp"));
		repositories.add(new Repository("C:/Temp/git/netty-http-client"));
		repositories.add(new Repository("C:/Temp/git/google-http-java-client"));
		return repositories;
	}
	
	public static List<Repository> getTicTacToeRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(new Repository("C:/Temp/git/ticTacToe"));
		repositories.add(new Repository("C:/Temp/git/TicTacToe-MVVM"));
		repositories.add(new Repository("C:/Temp/git/ticTacToe2"));
		repositories.add(new Repository("C:/Temp/git/Tic-Tac-Toe"));
		repositories.add(new Repository("C:/Temp/git/ticTacToe3"));
		repositories.add(new Repository("C:/Temp/git/tic-tac-toe-android-app"));
		return repositories;
	}
	
	private static void writeOutputFile(String path, List<String> rows) throws IOException {
		Path outputPath = Paths.get(path);
		Files.write(outputPath, rows, Charset.forName("UTF-8"));
	}
}
