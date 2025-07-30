#!/usr/bin/node
const request = require('request');
request(process.argv[2], (e, r, b) => {
  if (!e) {
    const results = JSON.parse(b);
    const completed = {};
    results.forEach(t => {
      if (t.completed && completed[t.userId] === undefined) { completed[t.userId] = 1; } else if (t.completed) { completed[t.userId] += 1; }
    });
    console.log(completed);
  }
});
