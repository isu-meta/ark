
import os
from pathlib import Path

from unittest import TestCase

from arks_code.report import generate_tsv, write_tsv

class ReportTests(TestCase):
    input_xml = Path(os.getcwd(), "test", "example_ezid.xml")
    input_tsv = Path(os.getcwd(), "test", "example_report.tsv")
    output_tsv = Path(os.getcwd(), "test", "output_report.tsv")
    def setUp(self):
        self.tearDown()
    
    def tearDown(self):
        if Path(self.output_tsv).exists():
            os.remove(self.output_tsv)

    def test_generate_tsv(self):
        generated_dict = generate_tsv(str(self.input_xml))
        desired_dict = {"Title": 
                            ["Copy of a Letter from Louis Hermann Pammel to S. W. Beyer, November 24, 1919"],
                        "CDM collection number": ["p16001coll16"],
                        "CDM URL": ["http://cdm16001.contentdm.oclc.org/cdm/ref/collection/p16001coll16/id/398"],
                        "ARK": ["ark:/87292/w9033g"],
                       }
        self.assertEqual(generated_dict, desired_dict)

    def test_write_tsv(self):
        write_tsv(generate_tsv(str(self.input_xml)), self.output_tsv)
        with open(self.input_tsv, "r") as fh:
            desired_tsv = fh.read()

        with open(self.output_tsv, "r") as fh:
            generated_tsv = fh.read()

        self.assertEqual(generated_tsv, desired_tsv)
        
        
