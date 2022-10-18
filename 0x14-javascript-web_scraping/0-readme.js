#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, inputD) => {
  if (err) throw err;
    console.log(inputD.toString());
})
