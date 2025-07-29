<?php
$name = $_GET['name'];
// VULNERABLE: reflects unsanitized input
echo "<h1>Hello $name</h1>"; // CWE-79
?>