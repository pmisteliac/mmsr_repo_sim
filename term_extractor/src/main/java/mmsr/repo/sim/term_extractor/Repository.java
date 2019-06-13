package mmsr.repo.sim.term_extractor;

import java.io.File;
import java.util.Collection;

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
	
	@Override
	public String toString() {
		return this.name;
	}

}
