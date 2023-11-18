const divElem = document.querySelector('#target');
const htmlElem = `<li>First item</li><li>Second item</li><li>Third item</li>`;
divElem.innerHTML = htmlElem;

document.querySelector('#target').classList.add('my-list');