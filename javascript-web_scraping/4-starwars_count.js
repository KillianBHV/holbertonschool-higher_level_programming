#!/usr/bin/node
const request = require('request');
request(process.argv[2], (e, r, b) => {
  if (!e) {
    const results = JSON.parse(b).results;
    console.log(results.reduce((count, movie) => {
      if (movie.characters.find(c => c.endsWith('/18/'))) { return count + 1; }
      return count;
    }, 0));
  }
});
