'use strict'


const inputti = prompt("Anna nimesi: ");

const ryhmat = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'];
const randomNumero = Math.floor(Math.random() * 4) + 1;

let randomRyhma;
switch (randomNumero) {
  case 1:
    randomRyhma = ryhmat[0];
    break;
  case 2:
    randomRyhma = ryhmat[1];
    break;
  case 3:
    randomRyhma = ryhmat[2]
    break;
  case 4:
    randomRyhma = ryhmat[3]
    break;
}


const elementti = document.querySelector('#kohde')

elementti.innerHTML = `Moikka ${inputti}! Ryhmäsi on ${randomRyhma}.`;
