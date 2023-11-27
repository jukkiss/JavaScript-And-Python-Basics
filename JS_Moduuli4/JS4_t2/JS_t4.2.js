'use strict'
const formi = document.querySelector('#query').parentElement;
formi.addEventListener('submit', async function(event){
    event.preventDefault();
    const haku = document.getElementById("query").value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${haku}`);
        const jsonData = await response.json();
        console.log(jsonData);
    } catch (error) {
        console.log(error.message);
    }
});

