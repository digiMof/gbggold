xquery version "3.0";

declare namespace tei="http://www.tei-c.org/ns/1.0";

declare function local:howManyPers($node as node()) 
    {
    count($node/tei:p/tei:persName)
    };

declare function local:howManyPlace($node as node()) 
    {
    count($node/tei:p/tei:placeName)
    };

declare function local:howManyThisPlace($node as node()) 
    {
    count($node/tei:p/tei:placeName[@ref='#ChiesaSGirolamo'])
    };

let $ourfile := doc("bassaniTei.xml")
    for $div in $ourfile/tei:TEI/tei:text/tei:body/tei:div
        return (local:howManyThisPlace($div))
