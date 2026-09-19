console.log("Ordem crescente")
let linha = '';
for (let numero = 0; numero < 100; numero++) {
  linha += String(numero).padStart(2,'0') +  " ";
  if ((numero + 1) % 10 == 0) {
    console.log(linha)
    linha = ''
  } 
}
console.log("Ordem decrescente")
for (let numero = 99; numero > -1; numero--) {
  linha += String(numero).padStart(2,'0') +  " ";
  if (numero % 10 == 0){
    console.log(linha)
    linha = ''
  } 
}
console.log("ímpares de 99 até 00 de 5 em 5")
for (let numero = 99; numero > -1; numero--) {
  if (numero % 2 == 1) {
    linha += String(numero).padStart(2, '0') + ' ';
  }
  if ((numero - 1) % 5 == 0 && (numero -1) % 10 ==0) {
    console.log(linha)
    linha = ''
  }
}

