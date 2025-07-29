
const express = require('express');
const app = express();
app.get('/', (req,res)=>{
  const name = req.query.name;
  // VULNERABLE: reflects unsanitized input
  res.send(`<h1>Hello ${name}</h1>`); // CWE-79
});
