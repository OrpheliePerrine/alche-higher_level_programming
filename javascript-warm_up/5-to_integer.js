#!/usr/bin/node
const arg = process.argv[2];
const n = parseInt(arg);

if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number:', n);
}
