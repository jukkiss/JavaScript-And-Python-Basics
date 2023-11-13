'use strict'

const inputti = prompt("Anna nimesi: ");

const ryhmat = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'];
const randomRyhma = ryhmat[Math.floor(Math.random() * ryhmat.length)];

const elementti = document.querySelector('#kohde')

elementti.innerHTML = `Moikka ${inputti}! Ryhmäsi on ${randomRyhma}.`;
