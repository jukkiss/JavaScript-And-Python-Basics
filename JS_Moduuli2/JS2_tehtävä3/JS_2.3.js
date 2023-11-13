'use strict';

const koirienNimet = [];

for (let i = 0; i < 6; i++) {
    koirienNimet.push(prompt(`Anna koiran nimi: ${i+1}:`));
}

koirienNimet.sort().reverse();

const teeLista = document.createElement("ul");

for (let i = 0; i < 6; i++) {
    const listaan = document.createElement("li");
    listaan.textContent = koirienNimet[i];
    teeLista.appendChild(listaan);
}

document.body.appendChild(teeLista);