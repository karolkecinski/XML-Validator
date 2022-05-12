from lxml import etree

class Validator:

    def __init__(self, xsd_path: str):
        XML_schema = etree.parse(xsd_path)
        self.XML_schema = etree.XMLSchema(XML_schema)

    def validate(self, xml_path: str) -> bool:
        XML_doc = etree.parse(xml_path)
        return self.XML_schema.validate(XML_doc)