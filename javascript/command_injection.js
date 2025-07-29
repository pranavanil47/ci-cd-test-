
const { exec } = require('child_process');
const dir = process.argv[2];
// VULNERABLE: unsanitized input to shell
exec(`ls ${dir}`, (e, stdout) => console.log(stdout)); // CWE-78
