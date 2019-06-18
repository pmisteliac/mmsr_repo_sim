package mmsr.repo.sim.term_extractor;

import java.io.File;
import java.util.Collection;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import org.apache.commons.io.FileUtils;


public final class Repository {
	
	private final String path;
	private final String name;
	
	public Repository (String path) {
		this.path = path;
		String[] parts = path.split("/");
		this.name = parts[parts.length - 1];
	}
	
	public Collection<File> getAllJavaFilePaths() {
		File repoDirectory = new File(this.path);
		String[] filterExtensions = {"java"};
		Collection<File> javaFiles = FileUtils.listFiles(repoDirectory, filterExtensions, true);
		return javaFiles;
	}
	
	public int getRepoSize() {
		return getAllJavaFilePaths().size();
	}
	
	public Collection<JavaCompilationUnit> getAllJavaCompilationUnits() {
		return this.getAllJavaFilePaths().stream()
				.map(file -> new JavaCompilationUnit(file))
				.collect(Collectors.toList());
	}
	
	public List<String> getAllTerms() {
		return this.getAllJavaCompilationUnits().stream()
				.flatMap(cu -> cu.getTerms().stream())
				.collect(Collectors.toList());
	}
	
	public String getCsvRepresentation() {
		String name = this.name + ";";
		List<String> terms = getAllTerms();
		return name + String.join(";", terms);
	}
	
	@Override
	public String toString() {
		return this.name;
	}

}
