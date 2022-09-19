# ESTE ARQUIVO FAZ PARTE DO ARQUIVO DA AULA 114ClassesAbstratasPythonPoo
# OS ARQUIVOS conta114 e contaCorrente TAMBÉM FAZEM PARTE DA AULA 114ClassesAbstratasPythonPoo


from classes114.conta114 import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:  # Verificando se o saldo na conta é menor que o valor que ela deseja sacar
            print('Saldo insuficiente')
            return

        self.saldo -= valor  # Se não, subtrai o valor do saldo pelo valor de saque
        self.detalhes()


