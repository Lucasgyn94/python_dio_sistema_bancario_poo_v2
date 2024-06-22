class ContaIterador:
    def __init__(self, cliente):
        self._cliente = cliente
        self._indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._indice < len(self._cliente.contas):
            conta = self._cliente.contas[self._indice]
            self._indice += 1
            return {
                "numero": conta.numero_conta,
                "agencia": conta.agencia,
                "saldo": conta.saldo
        } 
        else:
            raise StopIteration
        