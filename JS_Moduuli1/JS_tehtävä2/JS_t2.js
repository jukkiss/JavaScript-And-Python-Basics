'use strict'
const inputti = prompt("Anna nimesi: ");

const elementti = document.querySelector('#kohde')

elementti.innerHTML = `Moikka ${inputti}!`;
