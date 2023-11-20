'use strict'

const numerot = []

for (let i = 0; i<5; i++) {
    const numero = +prompt(`Anna numero:`);
    numerot.push(numero);
}

for (let i = numerot.length - 1; i>= 0; i--) {
    console.log(numerot[i]);
}

/*
const numerot = [];

for (let i = 0; i < 5; i++) {
    const numero = prompt(`Anna numero ${i + 1}:`);
    numerot.push(numero);
}

for (let i = numerot.length - 1; i >= 0; i--) {
    console.log(numerot[i]);
}
*/