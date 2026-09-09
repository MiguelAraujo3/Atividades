function soma1(param1, param2 = 0) {
    sum = param1 + param2
    console.log(typeof(param2))
    return sum
}
const soma2 = function(param1, param2) {return param1 + param2};

let soma3 = (param1, param2) => param1 +param2

const soma4 = (param1, param2) => { return param1 +param2 }
function soma5(param1, param2, callback) {
  resultado = callback(param1, param2)
  return resultado
}
function soma6(param1, ...params) {
  console.log(Array.isArray(params))
  console.log(typeof(params))
  return param1 + params
}
console.log("forma tradicional " + soma1(1,1))
console.log("função anonima, armazenada dentro de variavel "  + soma2(1,1))
console.log("arrow function " + soma3(1,1))
console.log("arrow funciton com return " + soma4(1,1))
console.log("testes chamando funções no callback " + soma5(1,3,soma3))

console.log(" teste sem colocar o segundo parametro forma tradicional " + soma1(1))
console.log(" teste sem colocar o segundo parametro função anonima, armazenada dentro de variavel "  + soma2(1))
console.log(" teste sem colocar o segundo parametro arrow function " + soma3(1))
console.log(" teste sem colocar o segundo parametro arrow funciton com return " + soma4(1))

console.log(`teste colocando crase para colocar variaveis resutlado da soma: ${soma1(1,2)}`)
console.log(`parametros rest "...parametros" ela concatena ${soma6(11,1)}`)

// começando array e seus métodos

const frutas = ["maçã", "péra", "banana "]
const vazio = []
const numeros1 = new Array(10,20,30 );
const from = Array.from("cachorro ")
console.log(frutas + vazio + numeros1 + from)
from.length = 4
console.log(from)

const numeros2 = [1,2,3,10,10]
console.log(numeros2.map(soma2))
console.log(numeros2)

console.log(numeros2.slice(2))
console.log(numeros2.find(n => n > 7))
console.log(numeros2.reverse())
console.log(numeros2.sort())