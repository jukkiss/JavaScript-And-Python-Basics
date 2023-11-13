'use strict'

const numerot = [];

while (true) {
    const inputti = prompt('Anna numero, nolla lopettaa:');
    if (inputti === '0') {
        break;
    }

    numerot.push(Number(inputti));
}

numerot.sort((a, b) => b - a);

console.log(numerot);