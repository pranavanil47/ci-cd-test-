
// VULNERABLE: hard-coded JWT secret
module.exports = { jwtSecret: 'supersecretkey' }; // CWE-798
