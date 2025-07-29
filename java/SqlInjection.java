
import java.sql.*;
public class SqlInjection {
    public void getUser(String userId) throws SQLException {
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/test", "root", "password");
        // VULNERABLE: user input directly concatenated into SQL query
        String query = "SELECT * FROM users WHERE id=" + userId; // CWE-89
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);
    }
}