# ESTE ARQUIVO FAZ PARTE DO ARQUIVO DA AULA 114ClassesAbstratasPythonPoo
# OS ARQUIVOS conta114 e contaPoupanca TAMBÉM FAZEM PARTE DA AULA 114ClassesAbstratasPythonPoo


from classes114.conta114 import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite= limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self._limite) < valor:  # Verificando se o saldo na conta é menor que o valor que ela deseja sacar
            print('Saldo insuficiente')
            return

        self.saldo -= valor  # Se não, subtrai o valor do saldo pelo valor de saque
        self.detalhes()