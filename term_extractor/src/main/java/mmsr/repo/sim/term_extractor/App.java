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
	
	public static final String REPO_DIR = "C:/Temp/git/";
	
	public static void main(String[] args) {
//		tryOutStuff();
		generateCsv();
	}
	
	private static void tryOutStuff() {
		Repository repo = createRepo("neo4j-java-driver");
		Collection<JavaCompilationUnit> allJavaCompilationUnits = repo.getAllJavaCompilationUnits();
		allJavaCompilationUnits.stream().forEach(cu -> System.out.println(cu.getComments()));
		System.out.println(repo.getTermOccurances());
	}
	
	private static void generateCsv() {
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
	}

	public static List<Repository> getRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.addAll(getHttpRepositories());
		repositories.addAll(getTicTacToeRepositories());
		repositories.addAll(getDbDriverRepositories());
		repositories.addAll(getCalendarRepositories());
		repositories.addAll(getOAuthRepositories());
		return repositories;
	}
	
	public static List<Repository> getHttpRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(createRepo("httputil"));
		repositories.add(createRepo("http-client"));
		repositories.add(createRepo("async-http-client"));
		repositories.add(createRepo("http-request"));
		repositories.add(createRepo("okhttp"));
		repositories.add(createRepo("netty-http-client"));
		repositories.add(createRepo("google-http-java-client"));
		return repositories;
	}
	
	public static List<Repository> getTicTacToeRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(createRepo("ticTacToe"));
		repositories.add(createRepo("TicTacToe-MVVM"));
		repositories.add(createRepo("ticTacToe2"));
		repositories.add(createRepo("Tic-Tac-Toe"));
		repositories.add(createRepo("ticTacToe3"));
		repositories.add(createRepo("tic-tac-toe-android-app"));
		return repositories;
	}
	
	public static List<Repository> getDbDriverRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(createRepo("sqlite-jdbc"));
		repositories.add(createRepo("neo4j-java-driver"));
		repositories.add(createRepo("arangodb-java-driver"));
		repositories.add(createRepo("snowflake-jdbc"));
		repositories.add(createRepo("mssql-jdbc"));
		return repositories;
	}
	
	public static List<Repository> getCalendarRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(createRepo("google-http-java-client"));
		repositories.add(createRepo("EasyCalendar"));
		repositories.add(createRepo("android-calendar-card"));
		repositories.add(createRepo("Material-Calendar-View"));
		repositories.add(createRepo("calendar"));
		repositories.add(createRepo("Etar-Calendar"));
		repositories.add(createRepo("CosmoCalendar"));
		repositories.add(createRepo("CalendarListview"));
		return repositories;
	}
	
	public static List<Repository> getOAuthRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(createRepo("signpost"));
		repositories.add(createRepo("scribejava"));
		repositories.add(createRepo("spring-security-oauth"));
		repositories.add(createRepo("apis"));
		repositories.add(createRepo("oauth2-shiro"));
		repositories.add(createRepo("oauth2-server"));
		return repositories;
	}
	
	private static Repository createRepo(String name) {
		return new Repository(REPO_DIR + name);
	}
	
	private static void writeOutputFile(String path, List<String> rows) throws IOException {
		Path outputPath = Paths.get(path);
		Files.write(outputPath, rows, Charset.forName("UTF-8"));
	}
}
