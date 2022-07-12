<?xml version="1.0" encoding="utf-8" standalone="no"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" 
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:str="xalan://java.lang.String"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:wikidata="https://www.wikidata.org/wiki/"
    xmlns:geonames="https://www.geonames.org/"
    xmlns:viaf="http://viaf.org/viaf/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/" exclude-result-prefixes="xs" version="1.0">
     
    <xsl:output method="html" encoding="UTF-8" indent="yes" />
    
    <xsl:template name="rdf">
        <xsl:param name="id"/>
        <!--<xsl:value-of select="//tei:xenoData/rdf:RDF/rdf:Description[@tei:ref = $id]/rdfs:label"/>  -->
            <xsl:value-of select="//tei:xenoData/rdf:RDF/rdf:Description[@tei:ref = $id]/@rdf:about"/> 
    </xsl:template>
    
    <xsl:template match="tei:place">                                                                              
        <li><xsl:value-of select="concat(tei:placeName/text(), ' ')" /> 
            <a> <xsl:attribute name="href">
                    <xsl:call-template name="rdf">
                        <xsl:with-param name="id" select="concat('#', @xml:id)" />
                    </xsl:call-template>
            </xsl:attribute><i class="bi bi-share-fill"></i>
            </a>
        </li>
        
    </xsl:template>
    
    <xsl:template match="tei:person">                                                                              
        <li><xsl:value-of select="concat(tei:persName/text(), ' ')" /> 
            <a> <xsl:attribute name="href">
                <xsl:call-template name="rdf">
                    <xsl:with-param name="id" select="concat('#', @xml:id)" />
                </xsl:call-template>
            </xsl:attribute><i class="bi bi-share-fill"></i>
            </a>
        </li>
        
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
                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" />
                 <!-- Bootstrap Font Icon CSS -->
                 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" />
                <script src="replace.js"></script> 
            </head>
            <body>
                <h1>Linked Open Data: Settings, Characters and Historical Figures in "Gli Occhiali d'Oro" by Bassani</h1><button onclick="replace()">set link</button>
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <h2>Places</h2>
                            <ul>
                                <xsl:apply-templates select="//tei:place" />
                            </ul>
                        </div>
                        <div class="col">
                            <h2>Person</h2>
                            <ul>
                                <xsl:apply-templates select="//tei:person" />
                            </ul>
                        </div>
                    </div>
                </div>
            </body>
        </html>
    </xsl:template>
    
</xsl:stylesheet>