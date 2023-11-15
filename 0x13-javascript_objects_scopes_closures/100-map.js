#!/usr/bin/node
const data = require('./100-data.js').list;
const res = data.map((value, index) => value * index);
console.log(data);
console.log(res);
