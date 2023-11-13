'use strict'

const osallistujienMaara = parseInt(prompt("Anna osallistujien määrä: "));
const osallistujat = [];

for (let i = 0; i < osallistujienMaara; i++) {
    osallistujat.push(prompt(`Anna osallistujan nimi ${i+1}:`));
}

osallistujat.sort();

const teeLista = document.createElement("ol");

for (let i = 0; i < osallistujienMaara; i++) {
    const listaan = document.createElement("li");
    listaan.textContent = osallistujat[i];
    teeLista.appendChild(listaan);
}

document.body.appendChild(teeLista);


