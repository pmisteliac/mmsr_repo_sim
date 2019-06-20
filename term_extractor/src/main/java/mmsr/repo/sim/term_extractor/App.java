package mmsr.repo.sim.term_extractor;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class App {
	
	public static final String REPO_DIR = "D:/git/";
	
	/*
	 * This has to be run with the G1 Garbage Collector
	 * VM Arguments: -Xmx4g -Xmx8g -XX:+UseG1GC
	 */
	public static void main(String[] args) {
		generateCsv(getAllRepositories(), "repos");
	}
	
	private static void generateCsv(List<Repository> repositories, String fileName) {
		List<String> repoCsvRows = repositories.stream()
				.map(repo -> repo.getCsvRepresentation())
				.collect(Collectors.toList());
		try {
			writeOutputFile("result/" + fileName + ".csv", repoCsvRows);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static List<Repository> getAllRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.addAll(getCuratedRepositories());
		repositories.addAll(getTopRepositories());
		return repositories;
	}
	

	public static List<Repository> getCuratedRepositories() {
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
	
	public static List<Repository> getTopRepositories() {
		List<Repository> repositories = new ArrayList<>();
		repositories.add(createRepo("RxJava"));
		repositories.add(createRepo("elasticsearch"));
		repositories.add(createRepo("retrofit"));
		repositories.add(createRepo("spring-boot"));
		repositories.add(createRepo("guava"));
		repositories.add(createRepo("MPAndroidChart"));
		repositories.add(createRepo("glide"));
		repositories.add(createRepo("spring-framework"));
		repositories.add(createRepo("butterknife"));
		repositories.add(createRepo("lottie-android"));
		repositories.add(createRepo("incubator-dubbo"));
		repositories.add(createRepo("zxing"));
		repositories.add(createRepo("EventBus"));
		repositories.add(createRepo("AndroidUtilCode"));
		repositories.add(createRepo("Android-Universal-Image-Loader"));
		repositories.add(createRepo("picasso"));
		repositories.add(createRepo("jadx"));
		repositories.add(createRepo("fresco"));
		repositories.add(createRepo("netty"));
		repositories.add(createRepo("libgdx"));
		repositories.add(createRepo("Hystrix"));
		repositories.add(createRepo("fastjson"));
		repositories.add(createRepo("BaseRecyclerViewAdapterHelper"));
		repositories.add(createRepo("material-dialogs"));
		repositories.add(createRepo("PhotoView"));
		repositories.add(createRepo("tinker"));
		repositories.add(createRepo("Material-Animations"));
		repositories.add(createRepo("plaid"));
		repositories.add(createRepo("SlidingMenu"));
		repositories.add(createRepo("jenkins"));
		repositories.add(createRepo("ExoPlayer"));
		repositories.add(createRepo("greenDAO"));
		repositories.add(createRepo("realm-java"));
		repositories.add(createRepo("logger"));
		repositories.add(createRepo("bazel"));
		repositories.add(createRepo("mybatis-3"));
		repositories.add(createRepo("dagger"));
		repositories.add(createRepo("guice"));
		repositories.add(createRepo("auto"));
		repositories.add(createRepo("junit4"));
		repositories.add(createRepo("mockito"));
		repositories.add(createRepo("javapoet"));
		repositories.add(createRepo("OpenRefine"));
		repositories.add(createRepo("j2objc"));
		repositories.add(createRepo("rebound"));
		repositories.add(createRepo("scribejava"));
		repositories.add(createRepo("moshi"));
		repositories.add(createRepo("socket.io-client-java"));
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
