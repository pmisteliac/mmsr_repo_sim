package mmsr.repo.sim.term_extractor;

import java.io.File;
import java.util.Collection;
import java.util.stream.Collectors;

import org.apache.commons.io.FileUtils;

import com.github.javaparser.ast.CompilationUnit;

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
	
	public Collection<JavaCompilationUnit> getAllJavaCompilationUnits() {
		return this.getAllJavaFilePaths().stream()
				.map(file -> new JavaCompilationUnit(file))
				.collect(Collectors.toList());
	}
	
	@Override
	public String toString() {
		return this.name;
	}

}
