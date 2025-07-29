
import java.nio.file.*;
public class PathTraversal {
    public byte[] readFile(String filename) throws Exception {
        // VULNERABLE: no validation allows directory traversal
        Path path = Paths.get("/var/www/uploads/" + filename); // CWE-22
        return Files.readAllBytes(path);
    }
}