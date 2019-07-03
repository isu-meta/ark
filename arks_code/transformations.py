from lxml import etree


def dctohtml():
    """
        Converts ContentDM's Dublin Core records into html
    """
    xslt_root = etree.XML(
        """\
    <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:dc="http://purl.org/dc/elements/1.1/">
    <xsl:template match="/">
        <table border="1">
            <tr>
                <th>url</th>
                <th>title</th>
                <th>publisher</th>
                <th>date</th>
                <th>type</th>
                <th>creator</th>
            </tr>
            <!-- TODO: Auto-generated template -->
            <xsl:apply-templates />
        </table>
    </xsl:template>
    <xsl:template match="rdf:RDF">
        <xsl:for-each select="rdf:Description">
            <tr>
                <td>
                    <xsl:value-of select="./@about" />
                </td>
                <td>
                    <xsl:value-of select="./dc:title" />
                </td>
                <td>
                    <xsl:value-of select="./dc:publisher" />
                </td>
                <td>
                    <xsl:value-of select="./dc:date" />
                </td>
                <td>
                    <xsl:value-of select="./dc:type" />
                </td>
                <td>
                    <xsl:value-of select="./dc:creator" />
                </td>
            </tr>
        </xsl:for-each>
    </xsl:template>
    </xsl:stylesheet>
    """
    )

    return etree.XSLT(xslt_root)


def formatupload(collection_number):
    """
        * Removes all test records with improper shoulder
        * formats transformation with collection number
    """
    xslt_root = etree.XML(
        """\
    <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xml:output indent="yes" />
    <xsl:template match="/">
        <!-- TODO: Auto-generated template -->
        <xsl:apply-templates select="*" />
    </xsl:template>
    <xsl:template match="*">
        <xsl:if test=".!=''">
            <xsl:copy>
                <xsl:copy-of select="@*" />
                <xsl:apply-templates />
            </xsl:copy>
        </xsl:if>
    </xsl:template>
    <xsl:template match="records">
        <records>
            <xsl:apply-templates />
        </records>
    </xsl:template>
    <xsl:template match="record">
        <xsl:for-each select='.'>
            <xsl:choose>
                <xsl:when
                    test="contains(./@identifier, 'ark:/99999')" />
                <xsl:when test="not(contains(element[@name = '_target'], '{}'))" />
                <xsl:otherwise>
                    <xsl:copy-of select="."></xsl:copy-of>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>
    </xsl:stylesheet>
    """.format(
            collection_number
        )
    )

    return etree.XSLT(xslt_root)


def formatxmltodict():
    """
        * The transformation for xml to python dictionary
    """
    xslt_root = etree.XML(
        """\
    <xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:strip-space elements="*" />
        <xsl:output omit-xml-declaration="yes" indent="no" />
        <xsl:template match="/">
            <xsl:apply-templates />
        </xsl:template>
        <xsl:param name="delim">
            <xsl:text>:</xsl:text>
        </xsl:param>
        <xsl:param name="quote">
            <xsl:text>'</xsl:text>
        </xsl:param>
        <xsl:template match='records'>
            <xsl:text>{</xsl:text>
            <xsl:for-each select='record'>
                <xsl:value-of select="$quote" />
                <xsl:value-of select='normalize-space(./element[@name="_target"])' />
                <xsl:value-of select="$quote" />
                <xsl:value-of select="$delim" />
                <xsl:value-of select="$quote" />
                <xsl:value-of select='./@identifier' />
                <xsl:value-of select="$quote" />,
            
            </xsl:for-each>
            <xsl:text>}</xsl:text>
        </xsl:template>
    </xsl:stylesheet>
    """
    )

    return etree.XSLT(xslt_root)


def remove_nan(x):
    if str(x) == "nan":
        return "undated"
    else:
        return x


def remove_xml_encoding(x):
    """
        Function to remove XML encoding
    """
    xml_rem = {
        ("&quot;", '"'),
        ("&apos;", "'"),
        ("&gt;", ">"),
        ("&lt;", "<"),
        ("&amp;", "&"),
    }
    for tup in xml_rem:
        x = x.replace(tup[0], tup[1])

    return x
