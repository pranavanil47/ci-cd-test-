using System.IO;
class PathTraversal {
    string Read(string file){
        // VULNERABLE: path concatenation
        return File.ReadAllText("C:/uploads/" + file); // CWE-22
    }
}