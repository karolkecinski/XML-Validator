from tokenize import String
import xmlschema as XMLS

class Validator:

    def __init__(self, xsd_path: str):
        self.XML_schema = XMLS.XMLSchema(xsd_path)

    def validate(self, xml_path: str) -> bool:
        return self.XML_schema.is_valid(xml_path)