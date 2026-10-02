function soma() {
  const param1 = Number(document.getElementById('idnumber1').value)
  const param2 = Number(document.getElementById('idnumber2').value)
  console.log(typeof(param1))
  const soma = param1 + param2
  document.querySelector('#resposta').textContent= soma
}

//document.querySelector('#botaoSomar').onclick = soma
document.querySelector('#botaoSomar').addEventListener('click', soma)