#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], pipe(fs.createWriteStream(process.argv[3], error => {
  if (error) console.log(error);
}));
