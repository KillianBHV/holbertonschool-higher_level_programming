#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, body) => {
  console.log(error || JSON.parse(body).title);
});
