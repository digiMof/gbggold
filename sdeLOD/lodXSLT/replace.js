const link = document.getElementsByTagName("a");
const regexpViaf = new RegExp("^viaf:");
const regexpWiki = new RegExp("^wikidata:");
const regexpGeonames = new RegExp("^geonames:");

function replace() {
      for (let i = 0; i < link.length; i++) {
            var currentLink = link[i].getAttribute("href");
            if (currentLink === "") {
                  link[i].remove();
            } else if (currentLink.match(regexpViaf)) {
                  var newlink = currentLink.replace(regexpViaf, "http://viaf.org/viaf/");
                  link[i].href = newlink
            } else if (currentLink.match(regexpWiki)) {
                  var newlink = currentLink.replace(regexpWiki, "https://www.wikidata.org/wiki/");
                  link[i].href = newlink
            } else if (currentLink.match(regexpGeonames)) {
                  var newlink = currentLink.replace(regexpGeonames, "https://www.geonames.org/");
                  link[i].href = newlink
            }
      }
}