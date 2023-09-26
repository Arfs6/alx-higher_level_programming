#!/usr/bin/node
request = require('request');

const endPoint = 'https://swapi-api.alx-tools.com/api/';
const id = process.argv[2];
request(`${endPoint}films/${id}`, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  film = JSON.parse(body);
  console.log(film.title);
});
