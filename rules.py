from pedido import Pedido

class Rules:
    _rulesArr = []

    def __init__(self, pedido):
        self._pedido = pedido
        self._rulesArr.append(self.validate_total_value)

    def validate(self):
        for r in self._rulesArr:
            if not r(self._pedido):
                return False
        return True
    
    def validate_total_value(self,pedido):
        if pedido.Valor_Total >= 80:
            return True
        return False