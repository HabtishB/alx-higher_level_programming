#!/usr/bin/node

const type = Number(process.argv[2]);

if (isNaN(type)) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(type));
}
