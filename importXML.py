import xml.etree.ElementTree as ET
from pedido import Pedido
from rules import Rules

def extract(xmlstr):
  pedido = Pedido()
  element = ET.fromstring(xmlstr) #le o documento xml e tranforma em um elementree
  
  total = element.find("Request/OrderRequest/OrderRequestHeader/Total/Money")
  pedido.Valor_Total = float(total.text.replace(",","."))
  
  pedido.Payload_Id = element.attrib['payloadID']

  pedido.Order_Id = element.find("Request/OrderRequest/OrderRequestHeader").attrib['orderID']

  pedido.From_Name = element.find("Header/From/Credential/Identity/Name").text
  pedido.From_Internal_Id = element.find("Header/From/Credential/Identity/InternalID").text

  rule = Rules(pedido)
  pedido.Response = 'accept' if rule.validate() else 'reject'

  return pedido

if __name__ == "__main__":
  with open('540.xml', 'r') as myfile:
    data=myfile.read()
    extract(data)
