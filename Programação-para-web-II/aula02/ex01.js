function maior(param1, param2) {
  if (param1 > param2) { 
    return "O Primeiro número é maior"
  } 
  else if (param1 < param2) {
    return "O Segundo número é maior"
  } else {
    return "Os número são iguais"
  }
}
console.log(maior(1,3))
console.log(maior(4,3))
console.log(maior(3,3))
console.log(maior(2,3))
