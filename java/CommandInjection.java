
public class CommandInjection {
    public static void main(String[] args) throws Exception {
        String userInput = args[0];
        // VULNERABLE: unsanitized input executed as part of system command
        Runtime.getRuntime().exec("sh -c 'ls " + userInput + "'"); // CWE-78
    }
}