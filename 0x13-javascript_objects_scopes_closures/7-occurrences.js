#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const filter = list.filter((el) => (el === searchElement));
  return filter.length;
};
