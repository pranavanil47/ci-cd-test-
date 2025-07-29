class HardcodedCreds {
    // VULNERABLE: hard-coded connection string
    const string CONN = "User ID=admin;Password=secret"; // CWE-798
}