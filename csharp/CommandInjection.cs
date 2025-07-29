using System.Diagnostics;
class CommandInjection {
    static void Main(string[] args){
        string dir = args[0];
        // VULNERABLE: unsanitized input to shell
        Process.Start("cmd.exe", "/C dir " + dir); // CWE-78
    }
}