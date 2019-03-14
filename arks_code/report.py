import re

from lxml import etree


def generate_tsv(xml_file):
    """Generate data for a TSV file.

    Generate data from an EZID XML File for
    writing to a tab-seperated-values file.

    Parameters
    ----------
    xml_file : str
        The path to the XML file to be processed.

    Returns
    -------
    dict
        A dictionary with keys representing the TSV column
        headers. Each key's value is a list containing
        the values for the TSV's columns.
    """
    coll_num_p = re.compile(r"(p1\d\d\d\dcoll\d\d)")
    tree = etree.parse(xml_file)
    tsv_content = {
        "Title": [e.text for e in tree.xpath("//element[@name='dc.title']")],
        "CDM collection number": [
            n.group(1) if n is not None else ""
            for n in [
                coll_num_p.search(e.text)
                for e in tree.xpath("//element[@name='_target']")
            ]
        ],
        "CDM URL": [e.text for e in tree.xpath("//element[@name='_target']")],
        "ARK": tree.xpath("//record/@identifier"),
    }

    return tsv_content


def write_tsv(tsv_dictionary, out_file):
    """Write a dictionary to a TSV file.

    Accepts a dictionary of lists and writes it to
    a tab-seperated-values file.

    Parameters
    ----------
    tsv_dictionary : dict
        A dictionary with keys representing the TSV column
        headers. Each key's value is a list containing
        the values for the TSV's columns.
    out_file : str
        The path to the XML file to be processed.

    Returns
    -------
    None
    """

    with open(out_file, "w", encoding="utf-8") as fh:
        fh.write("Title\tCDM collection number\tCDM URL\tARK\n")
        for i in range(len(tsv_dictionary["ARK"])):
            fh.write(
                f"{tsv_dictionary['Title'][i]}\t{tsv_dictionary['CDM collection number'][i]}\t{tsv_dictionary['CDM URL'][i]}\t{tsv_dictionary['ARK'][i]}\n"
            )
