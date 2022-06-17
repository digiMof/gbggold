var map = L.map('map').setView([44.8345, 11.62], 14.5);

var osm = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

//ferrara
    //borghesia
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
    //fadigati prima
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
    //fadigati dopo
    acquedotto = L.polygon([[44.83736, 11.607281], [44.836866, 11.608364], [44.837832, 11.609169], [44.838304, 11.608944], [44.838228, 11.60815]], {color: '#f03'}),
    bomporto = L.polygon ([[44.831849, 11.621341], [44.831373, 11.620965]], {color: '#f03'}),
    vigne = L.polygon ([[44.831373, 11.620965], [44.833714, 11.617484]], {color: '#f03'}),
    ripagrande = L.polygon([[44.833584, 11.617307], [44.834478, 11.616079]], {color: '#f03'}), 
    ripagrande1 = L.polygon([[44.837453, 11.611766], [44.834478, 11.616079]], {color: '#f03'}), 
    montagnone = L.polygon ([[44.826108, 11.630797],[44.825971, 11.633093], [44.828171, 11.632406], [44.828269, 11.631935]], {color: '#f03'}),
    pontelagoscuro = L.polygon ([[44.871929, 11.612337], [44.895343, 11.617228]], {color: '#f03'}),
    //bassani narratore
    gbomporto = L.polygon ([[44.831849, 11.621341], [44.831373, 11.620965]], {color: '#8f00ff'}),
    gripagrande = L.polygon([[44.833584, 11.617307], [44.834478, 11.616079]], {color: '#8f00ff'}), 
    gripagrande1 = L.polygon([[44.837453, 11.611766], [44.834478, 11.616079]], {color: '#8f00ff'}),
    gmontagnone = L.polygon ([[44.826108, 11.630797],[44.825971, 11.633093], [44.828171, 11.632406], [44.828269, 11.631935]], {color: '#8f00ff'}),
    gsavonarola = L.polygon([[44.834316, 11.624084], [44.832216, 11.628128]], {color: '#8f00ff'}), 
    ggirolamo = L.polygon ([[44.832907, 11.626813], [44.831743, 11.626298]], {color: '#8f00ff'});

//rimini
//fadigati prima
var hotmarepineta = L.polygon([[44.271631, 12.351724],[44.271819, 12.352764],[44.270954, 12.352132],[44.271127, 12.352904]], {color: '#ffa500'}),
    hotbritannia = L.polygon([[44.198278, 12.407933],[44.19852, 12.408448], [44.198181, 12.408743], [44.197979, 12.408362]], {color: '#ffa500'}),
    //riccione
    caffezanarini = L.polygon([[43.996112, 12.650816], [44.003074, 12.661389]]), 
    vialemille = L.polygon([[44.003038, 12.653674], [44.000183, 12.656955]]);
//bologna
var comunale=L.polygon([[44.496176, 11.350422], [44.49644, 11.351043], [44.497014, 11.350528], [44.496831, 11.349933]], {color: '#ffa500'}),
    pgalliera=L.polygon([[44.504024, 11.344544], [44.503959, 11.344855], [44.504119, 11.344919], [44.504181, 11.344662]], {color: '#ffa500'}), 
    collesluca=L.polygon([[44.47884, 11.297649], [44.478779, 11.298764], [44.479315, 11.298678], [44.479284, 11.297777]], {color: '#ffa500'}), 
    piazzastazione=L.polygon([[44.505325, 11.342661], [44.505164, 11.34369], [44.505631, 11.343803], [44.505768, 11.342779]], {color: '#ffa500'}),
    zamboni1=L.polygon([[44.494529, 11.34683],[44.494912, 11.347227]], {color: '#ffa500'}), 
    zamboni2=L.polygon([[44.494912, 11.347227], [44.498191, 11.355897]], {color: '#ffa500'}), 
    indipendenza=L.polygon([[44.494908, 11.3425744],[44.504535, 11.345464]], {color: '#ffa500'}), 
    stmaggiore=L.polygon([[44.494207, 11.346473], [44.490166, 11.356992]], {color: '#ffa500'}),
    duetorri=L.polygon([[44.494207, 11.346473], [44.494454, 11.346712], [44.494355, 11.347055], [44.494056, 11.34684]], {color: '#ffa500'}),
    pasticceriamajani=L.polygon([[44.491315, 11.341029],[44.491315, 11.340868], [44.491378, 11.340863], [44.491387, 11.340991]], {color: '#ffa500'}),
    sanvitale=L.polygon([[44.494454, 11.346712],[44.49401, 11.356577]], {color: '#ffa500'}),
    //studenti
    scomunale=L.polygon([[44.496176, 11.350422], [44.49644, 11.351043], [44.497014, 11.350528], [44.496831, 11.349933]]),
    spgalliera=L.polygon([[44.504024, 11.344544], [44.503959, 11.344855], [44.504119, 11.344919], [44.504181, 11.344662]]), 
    scollesluca=L.polygon([[44.47884, 11.297649], [44.478779, 11.298764], [44.479315, 11.298678], [44.479284, 11.297777]]), 
    spiazzastazione=L.polygon([[44.505325, 11.342661], [44.505164, 11.34369], [44.505631, 11.343803], [44.505768, 11.342779]]),
    szamboni1=L.polygon([[44.494529, 11.34683],[44.494912, 11.347227]]), 
    szamboni2=L.polygon([[44.494912, 11.347227], [44.498191, 11.355897]]), 
    sindipendenza=L.polygon([[44.494908, 11.3425744],[44.504535, 11.345464]]), 
    sstmaggiore=L.polygon([[44.494207, 11.346473], [44.490166, 11.356992]]),
    sduetorri=L.polygon([[44.494207, 11.346473], [44.494454, 11.346712], [44.494355, 11.347055], [44.494056, 11.34684]]),
    spasticceriamajani=L.polygon([[44.491315, 11.341029],[44.491315, 11.340868], [44.491378, 11.340863], [44.491387, 11.340991]]),
    ssanvitale=L.polygon([[44.494454, 11.346712],[44.49401, 11.356577]]);

var casastudio = L.marker([44.835579, 11.621328]).bindPopup('Casa-Studio Fadigati').addTo(map);
var suicidio = L.marker ([44.888008, 11.615381]).bindPopup('Suicidio Fadigati').addTo(map);

var borghesia = L.layerGroup([castellonord, piazzaerbe, giovecca, roma, bersaglieripo, sancarlo, cattedrale, mazzini, garganello, garibaldi4, garibaldi5, cunione, cnegozianti]).addTo(map);
var fadigati_prima = L.layerGroup([fcastellonord, fpiazzaerbe, fgiovecca, froma, fbersaglieripo, fsancarlo, fcattedrale, fmazzini, fsaraceno, fgarganello, fgaribaldi1, fgaribaldi2, fsanromano, fsanromanobis, fptravaglio, fcunione, fcnegozianti, comunale, pgalliera, collesluca, piazzastazione, zamboni1, zamboni2, indipendenza, stmaggiore, duetorri, pasticceriamajani, sanvitale]);
var fadigati_dopo = L.layerGroup([fgaribaldi1bis, fgaribaldi2bis, acquedotto, bomporto, vigne, ripagrande, ripagrande1, montagnone, pontelagoscuro]);
var bassani_dopo = L.layerGroup([gbomporto, gripagrande, gripagrande1, gmontagnone, gsavonarola, ggirolamo]); 
var studenti = L.layerGroup([scomunale, spgalliera, scollesluca, spiazzastazione, szamboni1, szamboni2, sindipendenza, sstmaggiore, sduetorri, spasticceriamajani, ssanvitale])

var baseMaps = {"Open Street Map": osm};
var overlayMaps = {"Borghesia": borghesia};

var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map); 
layerControl.addOverlay(fadigati_prima, "Fadigati prima");
layerControl.addOverlay(studenti, "Studenti")
layerControl.addOverlay(fadigati_dopo, "Fadigati dopo");
layerControl.addOverlay(bassani_dopo, "Bassani dopo");




