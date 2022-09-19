import re


class CalculoIpv4():
    def __init__(self, ip, mascara=None, cidr=None):
        self._ip = ip
        self._mascara = mascara
        self._cidr = cidr

        self.ipPart1 = 0
        self.ipPart2 = 0
        self.ipPart3 = 0

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def cidr(self):
        return self._cidr


    def removeCaracteres(self):

        ip = self._ip.split('.')
        print(ip)
        return ip


    def binarios(self):


        ip = self.removeCaracteres()
        contador = 8
        print(ip)
        binarios = []
        for i in ip:
            #192.168.0.25
            lista = []
            var = int(i)
            soma = 128

            while len(lista) < contador:

                if soma < int(i):
                    lista.append(0)
                    soma = soma / 2

                else:
                    if (var % 2) == 0:
                        lista.append(0)


                    else:
                        lista.append(1)
                        soma = soma / 2

                var = var / 2

            binarios.append(lista[::-1])

        print(binarios)



ip = CalculoIpv4('192.168.0.25')
ip.binarios()

print(f'resto: {128 % 2}')