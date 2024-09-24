window.onload = init;

function init() {
  //map
  const map = L.map("map").setView([51.509865, -0.118092], 6);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  // featch api get request
  const fetchGetRequest = async (url, func) => {
    try {
      const response = await fetch(url);
      const json = await response.json();
      return func(json);
    } catch (error) {
      console.log(error.message);
    }
  };

  const addToMapp = json => {
    L.geoJSON(json, {}).addTo(map);
  };

  //fetchGetRequest("/backend/areas/", addToMapp);
  fetchGetRequest("/backend/sight", addToMapp);



 // end of initialization 
}