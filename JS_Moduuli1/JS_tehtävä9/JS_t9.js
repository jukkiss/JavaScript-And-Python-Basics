'use strict'

const luku = prompt("Anna kokonaisluku: ");

let alkuluku = 'on';

if(luku !== 1) {
    for (let i = 2; i < luku; i++) {
        const jakojaannos = luku % i;
        if (jakojaannos === 0) {
         alkuluku = 'ei ole';
         break;
        }
    }
} else {
    alkuluku = 'ei ole';
}

document.querySelector('#kohde').innerHTML = `${luku} ${alkuluku} alkuluku.`

