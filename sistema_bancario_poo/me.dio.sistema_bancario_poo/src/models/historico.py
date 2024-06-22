from datetime import datetime

class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes

    def adicionar_transacao(self, tipo, valor):
        self.__transacoes.append({
            "tipo": tipo,  # Usa o tipo passado como argumento
            "valor": valor,
            "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S")
        })

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self.__transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self.__transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes