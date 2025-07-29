<?php
$file = $_GET['file'];
// VULNERABLE: unsanitized input in shell exec
system("cat $file"); // CWE-78
?>