import xml.etree.ElementTree as ET 

element = ET.parse('540.xml') #le o documento xml e tranforma em um elementree
total = element.findall("Request/OrderRequest/OrderRequestHeader/Total/Money")
for i in total:
  print (i.text)