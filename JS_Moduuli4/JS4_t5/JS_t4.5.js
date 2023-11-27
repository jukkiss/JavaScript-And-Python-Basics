'use strict'

const haku = 'https://api.chucknorris.io/jokes/random';
async function haeData() {
  try {
    const response = await fetch(
        haku
    );

    const jsonData = await response.json()

    kasitteleData(jsonData);

  } catch (error) {
    console.log(error.message);
  }

  function kasitteleData(jsonData) {
    console.log(jsonData.value);
  }
}

haeData();