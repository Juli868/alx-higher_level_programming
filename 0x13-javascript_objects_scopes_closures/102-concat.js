#!/usr/bin/node
const file = require('fs');
file.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  const first = data;
  file.readFile(process.argv[3], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    }
    const second = data;
    const combined = first + second;
    file.writeFile(process.argv[4], combined, err => {
      if (err) {
        console.error(err);
      }
    });
  });
});
