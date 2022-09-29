from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #estamos criando uma relação com o usuario do django
    total = models.FloatField()
    qtd_total = models.PositiveIntegerField()

    status = models.CharField(#Neste caso, vai ser um atributo charfield, porém com opção de escolha. Será parecido com o
        # enum de banco de dados
        default="C",
        max_length=1, #terá tamanho de 1. Pois, apesar de que vamos escolher entre Variação e Simples, ele vai armazenar
        # 'A' ou 'C' ou 'R' e etc
        choices=(
            ('A', 'Aprovado'),  #se escolher variavel, ele manda um 'A'
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self): #lembrando que esse metodo serve apenas para mostrar o nome na tela de admin
        return f'Pedido N. {self.pk}'  #Aqui, ao inves de retornarmos somente o nome, estamos costumizando uma msg
    #concatenada com o id do pedido


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000) #aqui, nós não vamos inserir uma nova imagem, nós vamos usar a imagem
    #já existem do produto. Até por isso, estamos definindo o tamanho 2000 caracteres pois, como vamos pegar o caminho
    #da imagem, esse caminho pode ser muito grande

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:#Sabemos que os nomes, mesmo que singular, aparecem como plural na tela de admin. Por exemplo,
    #'variacao' apareceria como 'variacaos'. aqui estamos definindo para o singular e o plural para que o django não faça
    #isso automaticamente e mostre nome errado, tipo, 'variacaos'
        verbose_name = 'Item do pedido' #essas duas variaveis são genericas do django
        verbose_name_plural = 'Itens do pedido'