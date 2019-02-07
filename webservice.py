from flask import Flask, request,json
from importXML import *
from responseXML import *
from serviceSOAP import ResponseRequest
from log import WSLog
import time

app = Flask(__name__)

@app.route('/pedido', methods=['POST'])
def pedido():
    log = WSLog()
    try:
        xml = request.data
        pedido = extract(xml)
        log.log('Pedido recebido '+ pedido.Order_Id)
        file_pedido = open('pedidos/'+pedido.Order_Id+'_'+ str(time.time())+'.xml', 'a+')
        file_pedido.write(str(xml))
        xml_response = makeXML(pedido)
        req = ResponseRequest(xml_response)
        log.log('Pedido processado '+ pedido.Order_Id)
        xml_retorno = '<?xml version="1.0"?><Retorno><Status>ok</Status></Retorno>'
        return xml_retorno
        
    except Exception as e:
        log.logError(e)
        xml_retorno = '<?xml version="1.0"?><Retorno><Status>error</Status></Retorno>'
        return xml_retorno
    
