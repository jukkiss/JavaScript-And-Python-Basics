'use strict'

const teksti = document.querySelector('#trigger');
const kuva = document.querySelector('#target');

teksti.addEventListener('mouseover', function(){
  kuva.src = 'img/picB.jpg';
})

teksti.addEventListener('mouseout', function(){
  kuva.src = 'img/picA.jpg';
})