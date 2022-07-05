function showChap(id) {
    var current = document.getElementById(id);
    $(".chap").css("display", "none");
    current.style.display = "block";
}

function showChars() {
    var bar = document.getElementById('metadatabar');
    var listchars = document.getElementById("listchars");
    var listplaces = document.getElementById("listplaces");
    var labelchars = document.getElementById('labChars');
    var labelplaces = document.getElementById('labPlace');
    bar.style.width = "50%";
    listchars.style.display = "block";
    listplaces.style.display = "none";
    labelchars.style.color = "black";
    labelplaces.style.color = "gray";
}

function showPlace() {
    var bar = document.getElementById('metadatabar');
    var listchars = document.getElementById("listchars");
    var listplaces = document.getElementById("listplaces");
    var labelchars = document.getElementById('labChars');
    var labelplaces = document.getElementById('labPlace');
    bar.style.width = "100%";
    listchars.style.display = "none";
    listplaces.style.display = "block";
    labelchars.style.color = "black";
    labelplaces.style.color = "black";
}

function showList(id) {
    var x = document.getElementById(id);
    if (x.style.display === "none" || x.style.display === "") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function toggleCheck(btnSwitch, className, color) {
    if(document.getElementById(btnSwitch).checked === true){
        $(className).css('background-color', color);
    } else {
        $(className).css('background-color', "white");
    }
  }