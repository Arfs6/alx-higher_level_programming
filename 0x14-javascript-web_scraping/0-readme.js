#!/usr/bin/node
const fs = require('fs')
const filename = process.argv[2]

fs.readFile(filename, 'utf8', (err, content) => {
  if (err) {
    console.error(err)
    return;
  }
  console.log(content)
})
