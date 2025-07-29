using System.Data.SqlClient;
class SqlInjection {
    void GetUser(string id){
        using(var conn = new SqlConnection("Server=.;Database=Test;Trusted_Connection=True;")){
            // VULNERABLE: concatenated SQL
            var cmd = new SqlCommand("SELECT * FROM Users WHERE Id=" + id, conn); // CWE-89
            conn.Open();
            cmd.ExecuteReader();
        }
    }
}