'use strict';

const num1 = +prompt('Anna eka numero');
const num2 = +prompt('Anna toka numero');
const num3 = +prompt('Anna kolmas numero');

const sum= num1 + num2 + num3;
const product = num1 * num2 * num3;
const avg = sum / 3;
const avgf = avg.toFixed(2)

const elementti = document.querySelector('#kohde')

elementti.innerHTML = `Summa on ${sum}, tulo on ${product} ja keskiarvo on ${avgf}`;