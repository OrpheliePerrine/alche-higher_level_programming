#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = Math.max(...args);
  let secondMax = -Infinity;

  for (const num of args) {
    if (num !== max && num > secondMax) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}
