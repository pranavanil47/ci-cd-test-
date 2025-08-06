# Create Node.js application code
app_js_content = '''const express = require('express');
const lodash = require('lodash');
const moment = require('moment');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const validator = require('validator');
const helmet = require('helmet');
const cors = require('cors');
const morgan = require('morgan');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware with potential vulnerabilities
app.use(helmet()); // Outdated version
app.use(cors()); // Outdated version
app.use(morgan('combined')); // Potential log injection
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Route with vulnerable dependencies usage
app.get('/', (req, res) => {
    const userData = {
        timestamp: moment().format(),
        userAgent: req.headers['user-agent'],
        ip: req.ip
    };
    
    // Using vulnerable lodash version
    const processedData = lodash.merge({}, userData, req.query);
    
    res.json({
        message: 'Vulnerable Node.js app for Trivy testing',
        data: processedData,
        vulnerabilities: [
            'Express 4.16.0 - CVE-2022-24999',
            'Lodash 4.17.11 - Prototype pollution',
            'Moment 2.19.1 - ReDoS vulnerability',
            'JWT 8.3.0 - Algorithm confusion',
            'And many more...'
        ]
    });
});

// Route using JWT with vulnerable version
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    
    if (!validator.isEmail(username)) {
        return res.status(400).json({ error: 'Invalid email format' });
    }
    
    // Vulnerable bcrypt usage
    const hashedPassword = await bcrypt.hash(password, 10);
    
    // Vulnerable JWT signing
    const token = jwt.sign({ username }, 'secret', { algorithm: 'HS256' });
    
    res.json({ token, message: 'Login successful with vulnerable dependencies' });
});

app.listen(PORT, () => {
    console.log(`Vulnerable app running on port ${PORT}`);
    console.log('This app contains intentionally vulnerable dependencies for Trivy testing');
});

module.exports = app;
'''

with open("vulnerable-node-app/app.js", "w") as f:
    f.write(app_js_content)

print("Created app.js for Node.js vulnerable application")