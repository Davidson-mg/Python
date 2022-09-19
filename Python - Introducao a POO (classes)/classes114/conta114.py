
# ESTE ARQUIVO FAZ PARTE DO ARQUIVO DA AULA 114ClassesAbstratasPythonPoo
# OS ARQUIVOS ContaCorrente e contaPoupanca ContaPoupanca TAMBÉM FAZEM PARTE DA AULA 114ClassesAbstratasPythonPoo
# ABC significa abstract basic class. Toda classe abstrata precisa herdar de ABC

from abc import ABC, abstractmethod  # Para criar classes abstratas é necessario este import




class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

        @property
        def agencia \
                (self):  # Toda classe abstrata precisa ter pelo menos um metodo abstrado e, esse metodo dentro da classe abstrata
        # não precisa fazer nada, mas precisa existir, como é o caso aqui
            return self._agencia

        @property
        def conta(self):
            return self._conta

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, valor):  # Este metodo vai inserir novos valores de saldo em minha conta
            if not isinstance(valor, (int, float)):  # Vamos verificar se o valor passado na instancia é float ou int
                raise ValueError("Saldo precisa ser numérico")  # Se não for, retorna essa exceção

            self._saldo = valor  # Se o valor passado na instancia é flout ou int, seta o valor na variavel saldo

        def depositar(self, valor):
            if not isinstance(valor, (int, float)):  # Vamos verificar se o valor passado na instancia é float ou int
                raise ValueError("Valor do depósito precisa ser numérico")  # Se não for, retorna essa exceção

            self.saldo += valor  # Se o valor passado na instancia é flout ou int, seta o valor na variavel saldo
            self.detalhes()

        # Cada vez que for feito um deposito, o valor deve ser somado ao saldo

        def detalhes(self):
            print(f'Agência: {self.agencia}', end=' ')
            print(f'Conta: {self.conta}', end=' ')
            print(f'Saldo: {self.saldo}')

        @abstractmethod  # Classe abstrata que vai força a implementação dela nas classes que herdam de Conta
        def sacar(self, valor):
            pass

        # Não vamos implementar este metodo aqui pois tipos de contas diferentes possuem comportamento diferentes
