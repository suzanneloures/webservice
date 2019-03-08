# -*- coding: utf-8 -*-

from flask import Flask, request,json
from importXML import *
from responseXML import *
from serviceSOAP import ResponseRequest
from log import WSLog
import time
import sys
from waitress import serve

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/pedido', methods=['POST'])
def pedido():
    log = WSLog()
    try:
        xml = request.data
        pedido = extract(xml)
        log.log('Pedido recebido '+ pedido.Order_Id)
        pedido_log_name = pedido.Order_Id+'_'+ str(time.time())+'.xml'
        file_pedido = open('pedidos/'+pedido_log_name, 'a+')
        file_pedido.write(str(xml))
        file_pedido.close()
        xml_response = makeXML(pedido)
        file_resposta = open('respostas/'+pedido_log_name,'a+')
        file_resposta.write(xml_response)
        file_resposta.close()
        req = ResponseRequest(xml_response)
        response = req.send()
        log.log('\nResposta enviada. Status'+ str(response.status_code)+' conteudo:\n'+response.text)
        log.log('Pedido processado '+ pedido.Order_Id)
        xml_retorno = '<?xml version="1.0"?><Retorno><Status>ok</Status></Retorno>'
        return xml_retorno
        
    except Exception as e:
        log.logError(e)
        xml_retorno = '<?xml version="1.0"?><Retorno><Status>error</Status></Retorno>'
        return xml_retorno
    
serve(app, port=8080)