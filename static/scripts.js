"use strict";

const $cupcakeList = $("#cupcakes-list");


populateCupcakesList();


async function getCupcakeData() {
  let response = await axios.get("http://localhost:5000/api/cupcakes");
  return response.data.cupcakes;
}

//We need to get the promise from the API

//Then iterate over that data to populate the cupcake list

async function populateCupcakesList() {
  const cupcakeData = await getCupcakeData()
  for (let i = 0; i < cupcakeData.length; i++) {
    $cupcakeList.append(`<li>${cupcakeData[i].flavor} Size: ${cupcakeData[i].size} Rating: ${cupcakeData[i].rating}</li>`);
  }
}