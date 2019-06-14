package mmsr.repo.sim.term_extractor;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;

public class JavaCompilationUnit {
	
	private final CompilationUnit compilationUnit;
	private final String sourceCode;
	
	public JavaCompilationUnit(File file) {
		try {
			sourceCode = new String(Files.readAllBytes(file.toPath()));
			compilationUnit = StaticJavaParser.parse(sourceCode);
		} catch (IOException e) {
			throw new IllegalArgumentException("Couldn't read file", e);
		}
	}

	public String getSourceCode() {
		return sourceCode;
	}

	public CompilationUnit getCompilationUnit() {
		return compilationUnit;
	}
	
	public List<String> getTypeNames() {
		return compilationUnit.findAll(ClassOrInterfaceDeclaration.class).stream()
        .map(type -> type.getNameAsString())
        .collect(Collectors.toList());
	}
	
	public List<String> getMethodNames() {
		return compilationUnit.findAll(MethodDeclaration.class).stream()
        .map(type -> type.getNameAsString())
        .collect(Collectors.toList());
	}
	
	public List<String> getTerms() {
		List<String> terms = new ArrayList<>();
		terms.addAll(getTypeNames());
		terms.addAll(getMethodNames());
		return terms;
	}

}
