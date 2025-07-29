
public class Reflection {
    public Object create(String className) throws Exception {
        // VULNERABLE: unsafe reflection from user input
        Class<?> clazz = Class.forName(className); // CWE-470
        return clazz.getDeclaredConstructor().newInstance();
    }
}