#!/usr/bin/node

const number = process.argv.length;
console.log(number === 2 ? 'No argument' : process.argv[2]);
