#!/usr/bin/node
fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (e, source1) => {
  if (e) {
    console.log(e);
    return;
  }
  fs.readFile(process.argv[3], 'utf8', (e, source2) => {
    if (e) {
      console.log(e);
      return;
    }
    target = source1 + source2;
    fs.writeFile(process.argv[4], target, e => {
      if (e) {

      }
    });
  });
});
