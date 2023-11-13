#!/usr/bin/node

const args = process.argv.slice(2); // Exclude the first two elements which are the path and script name

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.map(Number).sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
