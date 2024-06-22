class Cliente:
    def __init__(self, endereco):
        self.contas = []
        self.endereco = endereco
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
       if len(conta.historico.transacoes_do_dia()) >= 2:
           print("\nVocê execedeu o número de transações permitidas para hoije!!")
           return
       
       transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    