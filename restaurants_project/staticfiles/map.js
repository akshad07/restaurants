const copy =
  "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
const url =
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, {
  attribution: copy,
});
const map = L.map("map", {
  layers: [layer],
  minZoom: 5,
});
map
  .locate()
  .on("locationfound", (e) =>
    map.setView(e.latlng, 8)
  )
  .on("locationerror", () =>
    map.setView([0, 0], 5)
  );

  
async function load_restaurants() {
    const restaurants_url = `/api/restaurants/?in_bbox=${map
      .getBounds()
      .toBBoxString()}`;
    const response = await fetch(
        restaurants_url
    );
    const geojson = await response.json();
    return geojson;
  }
  
  async function render_restaurants() {
    const restaurants = await load_restaurants();
    L.geoJSON(restaurants)
      .bindPopup(
        (layer) =>
          layer.feature.properties.name
      )
      .addTo(map);
  }
  
  map.on("moveend", render_restaurants);