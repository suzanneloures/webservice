import requests

class ResponseRequest():

    
    def __init__(self, xml):
        self._xml = xml
    

    def send(self):
        headers = {'Content-Type': 'text/xml',}
        response = requests.post('https://intwbs.webb.com.br:7010/webb-jboss-esb/ebws/buffer_WEBB/WBB_ROUTER_WS', headers = headers, data= self._xml)
        return response
        