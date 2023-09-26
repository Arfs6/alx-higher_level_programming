#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const results = JSON.parse(body).results;
  let count = 0;
  results.forEach(element => {
    element.characters.forEach(character => {
      if (character.endsWith('/18/')) {
        count += 1;
      }
    });
  });
  console.log(count);
});
