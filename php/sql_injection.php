<?php
$conn = new mysqli('localhost','root','password','test');
$id = $_GET['id'];
// VULNERABLE: concatenated SQL
$result = $conn->query("SELECT * FROM users WHERE id = $id"); // CWE-89
?>