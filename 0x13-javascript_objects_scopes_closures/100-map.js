#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list);

const map = list.map((el, index) => (el * index));

console.log(map);
