import xml.etree.ElementTree as ET
tree = ET.parse('562.xml')


root = tree.getroot()

for Credential in root.iter('Credential'):
    print Credential.attrib