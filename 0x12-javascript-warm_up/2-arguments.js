#!/usr/bin/node

if (process.argv) {
  if (process.argv.length <= 2) {
    console.log('No argument');
  } else if (process.argv.length === 3) {
    console.log('Argument Found');
  } else {
    console.log('Arguments Found');
  }
} else {
  console.log('No argument');
}
