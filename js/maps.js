var map = L.map('map').setView([44.8345, 11.62], 14.5);

var osm = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);


var castellonord = L.polygon([[44.838453, 11.619152],[44.837841, 11.620413]]),
    piazzaerbe = L.polygon([[44.835646, 11.619211], [44.835456, 11.619187], [44.834769, 11.621046], [44.834973, 11.621266]]),
    giovecca = L.polygon([[44.837841, 11.620413], [44.831876, 11.632923]]),
    roma    = L.polygon([[44.836034, 11.619383], [44.837841, 11.620413]]),
    bersaglieripo = L.polygon([[44.835498, 11.621593], [44.836856, 11.622591]]),
    sancarlo = L.polygon([[44.837746, 11.620823],[44.837689, 11.620976], [44.837845, 11.62114], [44.837902, 11.620941]]), 
    cattedrale = L.polygon ([[44.835988, 11.619732], [44.835574, 11.619485], [44.835113, 11.620987], [44.835517, 11.621255]]),
    mazzini = L.polygon ([[44.834752, 11.621046],[44.833284, 11.6225]]), 
    saraceno = L.polygon ([[44.833284, 11.6225], [44.832816, 11.623058]]), 
    garganello = L.polygon([[44.836034, 11.619383], [44.835498, 11.621593]]),
    garibaldi4 = L.polygon([[44.837627, 11.616405], [44.837118, 11.617478]]),
    garibaldi5 = L.polygon([[44.836296, 11.618427], [44.837118, 11.617478]]),
    cunione = L.polygon([[44.839712, 11.618382], [44.839638, 11.618248], [44.839507, 11.61849], [44.839602, 11.618586]]), 
    cnegozianti = L.polygon([[44.837295, 11.621848], [44.837238, 11.621966], [44.837369, 11.622065], [44.837415, 11.621963]]),
    fcastellonord = L.polygon([[44.838453, 11.619152],[44.837841, 11.620413]], {color: '#ffa500'}),
    fpiazzaerbe = L.polygon([[44.835646, 11.619211], [44.835456, 11.619187], [44.834769, 11.621046], [44.834973, 11.621266]], {color: '#ffa500'}),
    fgiovecca = L.polygon([[44.837841, 11.620413], [44.831876, 11.632923]], {color: '#ffa500'}),
    froma    = L.polygon([[44.836034, 11.619383], [44.837841, 11.620413]], {color: '#ffa500'}),
    fbersaglieripo = L.polygon([[44.835498, 11.621593], [44.836856, 11.622591]], {color: '#ffa500'}),
    fsancarlo = L.polygon([[44.837746, 11.620823],[44.837689, 11.620976], [44.837845, 11.62114], [44.837902, 11.620941]], {color: '#ffa500'}), 
    fcattedrale = L.polygon ([[44.835988, 11.619732], [44.835574, 11.619485], [44.835113, 11.620987], [44.835517, 11.621255]], {color: '#ffa500'}),
    fmazzini = L.polygon ([[44.834752, 11.621046],[44.833284, 11.6225]], {color: '#ffa500'}), 
    fsaraceno = L.polygon ([[44.833284, 11.6225], [44.832816, 11.623058]], {color: '#ffa500'}), 
    fgarganello = L.polygon([[44.836034, 11.619383], [44.835498, 11.621593]], {color: '#ffa500'}),
    fsanromano = L.polygon([[44.835147, 11.620022], [44.833709, 11.618981]], {color: '#ffa500'}),
    fsanromanobis = L.polygon([[44.832385, 11.617238], [44.833709, 11.618981]], {color: '#ffa500'}),
    fptravaglio = L.polygon([[44.832385, 11.617238], [44.832829, 11.616476], [44.833077, 11.61683], [44.832589, 11.617495]], {color: '#ffa500'}),
    fgaribaldi1 = L.polygon([[44.838929, 11.612227], [44.838825, 11.61307]], {color: '#ffa500'}),
    fgaribaldi2 = L.polygon([[44.838825, 11.61307],[44.837772, 11.615129]], {color: '#ffa500'}),
    fgaribaldi1bis = L.polygon([[44.838929, 11.612227], [44.838825, 11.61307]], {color: '#f03'}),
    fgaribaldi2bis = L.polygon([[44.838825, 11.61307],[44.837772, 11.615129]], {color: '#f03'}),
    fcunione = L.polygon([[44.839712, 11.618382], [44.839638, 11.618248], [44.839507, 11.61849], [44.839602, 11.618586]], {color: '#ffa500'}), 
    fcnegozianti = L.polygon([[44.837295, 11.621848], [44.837238, 11.621966], [44.837369, 11.622065], [44.837415, 11.621963]], {color: '#ffa500'}),
    acquedotto = L.polygon([[44.83736, 11.607281], [44.836866, 11.608364], [44.837832, 11.609169], [44.838304, 11.608944], [44.838228, 11.60815]], {color: '#f03'}),
    bomporto = L.polygon ([[44.831849, 11.621341], [44.831373, 11.620965]], {color: '#f03'}),
    vigne = L.polygon ([[44.831373, 11.620965], [44.833714, 11.617484]], {color: '#f03'}),
    ripagrande = L.polygon([[44.833584, 11.617307], [44.834478, 11.616079]], {color: '#f03'}), 
    ripagrande1 = L.polygon([[44.837453, 11.611766], [44.834478, 11.616079]], {color: '#f03'}), 
    montagnone = L.polygon ([[44.826108, 11.630797],[44.825971, 11.633093], [44.828171, 11.632406], [44.828269, 11.631935]], {color: '#f03'}),
    pontelagoscuro = L.polygon ([[44.871929, 11.612337], [44.895343, 11.617228]], {color: '#f03'}),
    gbomporto = L.polygon ([[44.831849, 11.621341], [44.831373, 11.620965]], {color: '#8f00ff'}),
    gripagrande = L.polygon([[44.833584, 11.617307], [44.834478, 11.616079]], {color: '#8f00ff'}), 
    gripagrande1 = L.polygon([[44.837453, 11.611766], [44.834478, 11.616079]], {color: '#8f00ff'}),
    gmontagnone = L.polygon ([[44.826108, 11.630797],[44.825971, 11.633093], [44.828171, 11.632406], [44.828269, 11.631935]], {color: '#8f00ff'}),
    gsavonarola = L.polygon([[44.834316, 11.624084], [44.832216, 11.628128]], {color: '#8f00ff'}), 
    ggirolamo = L.polygon ([[44.832907, 11.626813], [44.831743, 11.626298]], {color: '#8f00ff'});

var casastudio = L.marker([44.835579, 11.621328]).bindPopup('Casa-Studio Fadigati').addTo(map);

var borghesia = L.layerGroup([castellonord, piazzaerbe, giovecca, roma, bersaglieripo, sancarlo, cattedrale, mazzini, garganello, garibaldi4, garibaldi5, cunione, cnegozianti]).addTo(map);
var fadigati_prima = L.layerGroup([fcastellonord, fpiazzaerbe, fgiovecca, froma, fbersaglieripo, fsancarlo, fcattedrale, fmazzini, fsaraceno, fgarganello, fgaribaldi1, fgaribaldi2, fsanromano, fsanromanobis, fptravaglio, fcunione, fcnegozianti]);
var fadigati_dopo = L.layerGroup([fgaribaldi1bis, fgaribaldi2bis, acquedotto, bomporto, vigne, ripagrande, ripagrande1, montagnone, pontelagoscuro]);
var bassani_dopo = L.layerGroup([gbomporto, gripagrande, gripagrande1, gmontagnone, gsavonarola, ggirolamo]); 

var baseMaps = {"Open Street Map": osm};
var overlayMaps = {"Borghesia": borghesia};

var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map); 
layerControl.addOverlay(fadigati_prima, "Fadigati prima");
layerControl.addOverlay(fadigati_dopo, "Fadigati dopo");
layerControl.addOverlay(bassani_dopo, "Bassani dopo");    



