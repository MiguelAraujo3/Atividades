const funcionarios = [
  {
    name: "jubibelu",
    cargo: "gerente",
    salario: 2600,
    beneficios: ["vale alimentação", "vale transporte", "licença maternindade", "plano de saude"]
  },
  {
    name: "cleide",
    cargo: "operadora",
    salario: 1500,
    beneficios: ["vale transporte", "vale refeição"]
  }
]

for (const coisa of funcionarios) {
  console.log(`Nome: ${coisa.name}`)
  console.log(`Cargo: ${coisa.cargo}`)
  console.log("Benefícios: ")
  for (let beneficio of coisa.beneficios)
    console.log(beneficio)
}