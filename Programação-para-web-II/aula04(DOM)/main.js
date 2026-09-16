function desvendarCurso() {
    const curso = document.querySelector('input[name=curso]').value;
    document.querySelector('#resposta').textContent = curso;
} 
/*
document
 .querySelector('form')
 .addEventListener('submit', function(event) {
    event.preventDefault();
    desvendarCurso();
 }
 )

Código para mostrar sem o botão e com contagem minima
document
 .querySelector('input[name=curso]')
 .addEventListener('input', function(event) {
    document.querySelector('#resposta').textContent = '';
    if (event.target.value.length >=3)
        desvendarCurso();
 })
*/
//Código do onclick no arquivo de JavaScript
document.querySelector('#btnDesvendar').onclick = desvendarCurso;
/*
//Código para ativar a function
document
    .querySelector('#btnDesvendar')
    .addEventListener('click', function() {
        alert("Dados Desvendados")
        desvendarCurso();
    });

document
   .querySelector('#btnDesvendar')
   .addEventListener('click', function() {
    alert('O tratament foi finalizado')
   });
*/