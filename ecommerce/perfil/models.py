from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re

from utils.validacpf import valida_cpf

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField( #Neste caso, vai ser um atributo charfield, porém com opção de escolha. Será parecido com o
        # enum de banco de dados
        max_length=2, #terá tamanho de 2, pois, apesar de que vamos escolher entre nome de estados, ele vai armazenar
        # apenas a sigla, por exemplo 'mg' de minas gerais
        default='SP',
        choices= (  #quais serão as escolhas

            ('AC', 'Acre'), #se escolher essa variavel, ele manda um 'AC'
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),

        )

    )

    def __str__(self):
        return f'{self.usuario}'

    def clean(self): #Vamos criar nossas validações dos campos cpf e cep

        error_messages = {} #estamos criando essa variavel do tipo dicionario, que vai receber os erros caso caia
        #nas condicionais de validação abaixo e no final será passada como parametro na classe generica do Django
        #ValidationError de validações. Essa classe funciona com dicionarios, por isso nossa variavel de msgs de erro
        #precisa ser do tipo dicionario

        #validando o CPF
        if not valida_cpf(self.cpf): #esse valida_cpf é uma função que nós mesmos criamos importamos do arquivo
            # validacpf na pasta utils. Estamos passando o cpf digitado para ser validado nela

            error_messages['cpf'] = 'Digite um CPF válido' #Entre couchete estamos informamos o campo que vai receber
            #a msg e logo em seguida a msg em si
            #não vamos retornar nada, apenas armazenar. Se retornassemos, todas vez que o cliente digisse algum campo
            #errado, a exceção seria levatado. Neste caso, nós vamos armazenar as msgs de erro caso hajam exceções
            # e no final a gente mostra todas as msg de uma vez

        #validando o CEP
        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8: #estamos usando uma expressão regular para verificar
        #se têm algum caracter que não é numero dentro do cep e se o tamanho é menor que 8
            error_messages['cep'] = 'CEP inválido, digite os 8 digitos do CEP'

        if error_messages: #Caso tenha alguma msg de erro
            raise ValidationError(error_messages) #Chamando nossa classe generica do django ValidationError e passando
        #a variavel com as msgs erro. Essa Classe fará o trabalho de mostrar as msg pra gente


    class Meta:#Sabemos que os nomes, mesmo que singular, aparecem como plural na tela de admin. Por exemplo,
    #'variacao' apareceria como 'variacaos'. aqui estamos definindo para o singular e o plural para que o django não faça
    #isso automaticamente e mostre nome errado, tipo, 'variacaos'
        verbose_name = 'Pefil' #essas duas variaveis são genericas do django
        verbose_name_plural = 'Perfis'

