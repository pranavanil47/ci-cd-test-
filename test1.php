<?php
// WARNING: Intentionally vulnerable code. Do NOT use in production.

// 🧑‍💻 Hardcoded secret
$admin_password = "admin123";

// 🚨 SQL Injection Vulnerability
if (isset($_POST['username']) && isset($_POST['password'])) {
    $conn = new mysqli("localhost", "root", "", "testdb");
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $username = $_POST['username'];
    $password = $_POST['password'];

    // ❌ Vulnerable to SQL Injection
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "Login successful!<br>";
    } else {
        echo "Invalid credentials.";
    }

    $conn->close();
}

// ❌ Insecure File Upload
if (isset($_FILES['upload'])) {
    $target_path = "uploads/" . basename($_FILES['upload']['name']);
    if (move_uploaded_file($_FILES['upload']['tmp_name'], $target_path)) {
        echo "The file " . basename($_FILES['upload']['name']) . " has been uploaded.";
    } else {
        echo "There was an error uploading the file.";
    }
}

// ❌ Command Injection
if (isset($_GET['ping'])) {
    $ip = $_GET['ping'];
    echo "<pre>";
    system("ping -c 2 " . $ip); // ⚠️ Dangerous
    echo "</pre>";
}

// ❌ Exposing PHP Info (Sensitive Data Disclosure)
if (isset($_GET['debug'])) {
    phpinfo();
}
?>
⚠️ Vulnerabilities: