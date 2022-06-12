var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

/*var map = L.map('map').setView([44.84, 11.62], 14.5);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

var polygon = L.polygon([
    [44.838461, 11.619256],
    [44.838050, 11.620275]
]).addTo(map);

/*var castellonord = L.polygon([[44.838453, 11.619152],[44.837841, 11.620413]]).addTo(map),
    piazzaerbe = L.polygon([[44.835646, 11.619211], [44.835456, 11.619187], [44.834769, 11.621046], [44.834973, 11.621266]]).addTo(map),
    giovecca = L.polygon([[44.837841, 11.620413], [44.831876, 11.632923]]).addTo(map),
    roma    = L.polygon([[44.836034, 11.619383], [44.837841, 11.620413]]).addTo(map),
    garganello = L.polygon([[44.836034, 11.619383], [44.835498, 11.621593]]).addTo(map),
    cnegozianti = L.marker([44,8373085, 11,6218840]).addTo(map), 
    cunione = L.marker([44,8394938, 11,6186868]).addTo(map), 
    bersaglieripo = L.polygon([[44.835498, 11.621668], [44.836856, 11.622591]]).addTo(map), 
    sancarlo = L.polygon([[44.837746, 11.620823],[44.837689, 11.620976], [44.837845, 11.62114], [44.837902, 11.620941]]).addTo(map), 
    cattedrale = L.polygon ([[44.835988, 11.619732], [44.835574, 11.619485], [44.835113, 11.620987], [44.835517, 11.621255]]).addTo(map), 
    mazzini = L.polygon ([[44.834752, 11.621046],[44.833284, 11.6225]]).addTo(map), 
    saraceno = L.polygon ([[44.833284, 11.6225], [44.832816, 11.623058], [44.83269, 11.62383], [44.831526, 11.624206]]).addTo(map);




/*var borghesia = L.layerGroup([castellonord, piazzaerbe, giovecca, roma]);
var fadigati = L.layerGroup([garganello]);

var overlayMaps = {
    "Borghesia": borghesia, 
    "Fadigati": fadigati
};

var layerControl = L.control.layers(overlayMaps).addTo(map);