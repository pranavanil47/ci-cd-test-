
const express = require('express');
const multer  = require('multer');
const upload = multer({ dest: 'uploads/' });
const app = express();
app.post('/upload', upload.single('file'), (req,res)=>{
  // VULNERABLE: no file type validation
  res.send('Uploaded');
});
