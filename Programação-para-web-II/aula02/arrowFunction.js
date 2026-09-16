function teste(param1,callback, param2  = undefined, ) {
  return callback(param1);
}

console.log(teste(5, (param1, param2) => param1 * param2))