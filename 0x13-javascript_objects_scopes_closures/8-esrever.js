#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length; i++) {
    const rmEl = list.pop();
    list.splice(i, 0, rmEl);
  }
  return list;
};
