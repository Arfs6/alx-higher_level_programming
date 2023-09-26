#!/usr/bin/node
request = require('request');

url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', response.statusCode);
});