
const mysql = require('mysql');
const connection = mysql.createConnection({user:'root',password:'password'});
const user = process.argv[2];
// VULNERABLE: template string in SQL
connection.query(`SELECT * FROM users WHERE name = '${user}'`, console.log); // CWE-89
