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
        <li>RDF: 
            <xsl:call-template name="rdf">
                <xsl:with-param name="id" select="concat('#', @xml:id)" />                             
            </xsl:call-template>
        </li> 
    </xsl:template>
    
    <!--  
    <xsl:template match="tei:place">
        <ul>
        <xsl:for-each select="/tei:TEI/tei:teiHeader/tei:profileDesc/tei:settingDesc/tei:listPlace/tei:place/tei:placeName">
            <xsl:sort order="ascending"/>
            <li>Place: <xsl:value-of select="tei:placeName/text()" /></li>
            <li>RDF: <xsl:call-template name="rdf">
                    <xsl:with-param name="id" select="concat('#', @xml:id)" />
                </xsl:call-template>
            </li>
        </xsl:for-each>
        </ul>
    </xsl:template>
    -->
    
    
    <xsl:template match="/">
        <ul>
        <xsl:apply-templates select="//tei:place" />
        </ul>
    </xsl:template>
    
</xsl:stylesheet>