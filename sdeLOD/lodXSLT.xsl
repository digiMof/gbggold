<?xml version="1.0" encoding="utf-8" standalone="no"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" 
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:wikidata="https://www.wikidata.org/wiki/"
    xmlns:geonames="https://www.geonames.org/"
    xmlns:viaf="http://viaf.org/viaf/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/" exclude-result-prefixes="xs" version="1.0">          
    
    <xsl:template name="rdf">
        <xsl:param name="id"/>
        <!--<xsl:value-of select="//tei:xenoData/rdf:RDF/rdf:Description[@tei:ref = $id]/rdfs:label"/>-->    
        <xsl:value-of select="//tei:xenoData/rdf:RDF/rdf:Description[@tei:ref = $id]/@rdf:about"/>
    </xsl:template>
    
    <xsl:template match="tei:place">                                                                              
        <li>Place: <xsl:value-of select="tei:placeName/text()" /></li>
        <xsl:if test="//tei:xenoData/rdf:RDF/rdf:Description">
            <li>RDF: 
                <xsl:call-template name="rdf">
                    <xsl:with-param name="id" select="concat('#', @xml:id)" />
                </xsl:call-template>
            </li>
        </xsl:if>
    </xsl:template>
    
    <xsl:template match="/">
        <xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html&gt;</xsl:text>
        <xsl:variable name="title"
            select="/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
        <html>
            <head>
                <meta charset="utf-8"/>
                <meta name="description" content="TEI Sample"/>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <title>
                    <xsl:value-of select="$title"/>
                </title>
            </head>
            <body>
                <ul>
                    <xsl:apply-templates select="//tei:place" />
                </ul>
            </body>
        </html>
    </xsl:template>
    
</xsl:stylesheet>