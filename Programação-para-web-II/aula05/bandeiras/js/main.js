import flags from './model/flags.js';
const main = document.querySelector('main')

main.insertAdjacentHTML('beforebegin', '<h2> 250 Países </h2>');
main.insertAdjacentHTML('afterend','<h2> Termino </h2>');

const fragmento = document.createDocumentFragment();
//loadCardsAsHTML();
loadCardsAsElements()
function loadCardsAsElements() {
  flags.forEach(
    (elemento) => {
      const card = criarCard(elemento)
      fragmento.appendChild(card)
      console.log( card.firstChild )
    }
  )
}

function loadCardsAsHTML() {
  const cardsAsHTML = flags.map ( (elemento) => criarCardHTML(elemento));

  main.innerHTML = cardsAsHTML.join('\n')
}

main.appendChild(fragmento)

function criarCardHTML(flag) {
  return `
    <div class="flag col-2 my-2 text-center">
      <img src="${flag.image}" alt="${flag.name}">
      <p> "${flag.name}"</p>
    </div>
  `;
}
function criarCard(flag) {
  const template = document.querySelector('template');
  const clone = template.content.cloneNode(true);
  clone.querySelector('img').alt = flag.name;
  clone.querySelector('img').src = flag.image;
  clone.querySelector('p').textContent = flag.name;
  console.log( clone.toString() );
  return clone;
}