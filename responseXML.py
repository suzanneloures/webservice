from yattag import Doc, indent
from pedido import Pedido
from datetime import datetime

def makeXML(pedido):
    doc, tag, text = Doc().tagtext()

    doc.asis('<?xml version="1.0" encoding="iso-8859-1"?>')
    with tag('SOAP:Envelope', ('xmlns:SOAP','http://schemas.xmlsoap.org/soap/envelope/') ):
        doc.stag('SOAP:Header')
        with tag('SOAP:Body'):
            with tag('cXML', payload='1', timestamp=datetime.now().strftime('%d/%m/%Y %H:%M:%S')):
                with tag('Header'):
                    with tag('From'):
                        with tag('Credential'):
                            with tag('Name'):
                                text(pedido.From_Name)
                            with tag('InternalID'):
                                text(pedido.From_Internal_Id)
                    with tag('Sender'):
                        with tag('Credential'):
                            with tag('Identity'):
                                doc.stag('WebbHeader', cnpj='73291750775399', isvSequence=1, isvid='0620000', messageType='562')
                with tag('Request'):
                    with tag('ConfirmationRequest'):
                        doc.stag('ConfirmationHeader', noticeDate=datetime.now().strftime('%d/%m/%Y'), type=pedido.Response)
                        with tag('OrderReference', orderID=pedido.Order_Id):
                            doc.stag('DocumentReference', payloadID=pedido.Payload_Id)
    result = indent(
        doc.getvalue(),
        indentation = ' '*4,
        newline = '\r\n'
    )

    return result