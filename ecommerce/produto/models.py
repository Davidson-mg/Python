from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.utils.text import slugify

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True) #slug é um tipo de url. Digamos que eu tenha um produto
    # camiseta com o nome "camiseta preta é legal", no slug ficaria parecido com "camiseta-preta-e-legal-123"
    # (o numero seria por ex o id)

    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0, verbose_name='Preço Promo')
    
    tipo = models.CharField( #Neste caso, vai ser um atributo charfield, porém com opção de escolha. Será parecido com o
        # enum de banco de dados
        default='V', 
        max_length=1, #terá tamanho de 1. Pois, apesar de que vamos escolher entre Variação e Simples, ele vai armazenar
        # 'V' ou 'S'
        choices=( #quais serão as escolhas
            ('V', 'Variavel'), #se escolher essa variavel, ele manda um 'V'
            ('S', 'Simples'), #se eu escolher simples, ele manda um simples
        )
    )  

    def get_preco_formatado(self): #metodo para formatar o valores de preco, colocando o R$, substituindo '.' por ','
        #e permitindo apenas duas casas decimais. No arquivo de admin, em list_display, onde vc colocaria o atributo
        #preco_marketing, vc coloca agora o metodo get_preco_formatado
        return f'R$ {self.preco_marketing:.2f}'.replace('.', ',')
    get_preco_formatado.short_description = 'Preço' #Sem isso nos campos da variavel preco_marketing, apareceria o nome
    #do metodo get_preco_formatado. Dessa forma, vai aparecer 'preço'

    def get_preco_promocional(self):
        return f'R$ {self.preco_marketing_promocional:.2f}'.replace('.', ',')
    get_preco_promocional.short_description = 'Preço promocional'




    #o metodo abaixo é para redimensionar a img. Como ele é grande e pode ser usado em outro lugar
    #o ideal serial criar um arquivo especifico pra ele e depois fazer o importe quando necessario

    @staticmethod #este metodo não vai mecher em nada relacionado a classe, por isso estamos defindo como metodo estatico
    def resize_image(img_pil, new_width): #este metodo vai receber o nome da imagem e uma nova largura. Este metodo só
        #será chamado caso atender ao if dentro do metodo save abaixo que é um metodo generico do django

        img_full_path = os.path.join(settings.MEDIA_ROOT, img_pil.name) #estamos pegando o caminho completo
        img_pil = Image.open(img_full_path) #estamos armazenando o obj de imagem na variavel img_pil
        original_height, original_width = img_pil.size  #estamos armazenado a altura e lergura via metodo size da classe Image

        if original_width <= new_width: #caso o tamanho da img que estamos inserindo seja menor ou igual ao tamanho que
            #quero reduzir, ele fecha o processo. Além disso, esse if impede a img seja salva novamente toda vez que vc
            #editar e salvar o post,mesmo que seja para modificar algo que não tenha relação com a img,
            img_pil.close()
            return

        """
        Regra de 3 para achar a nova algura

        larguraOriginal alturaOriginal
        novaLargura          ??? 

        Multiplica cruzado novaLargura com alturaOriginal e divide o resultado por larguraOriginal
        """

        new_height = round((new_width * original_height) / original_width)
        new_image = img_pil.resize((new_width, new_height), Image.LANCZOS) #Redimensionando a imagem com os
        #novos valores. Esse LANCZOS é um caulo de como será reduzido a img em questão de pixel. Pode ler na
        #documentação do pillow

        new_image.save(
            img_full_path, #estamos reescrevendo a imagem do caminho iriginal
            optimiza=True,
            quality=60
        )
        print('Imagem foi redimensionada')

        new_image.close()

    def save(self, *args, **kwargs): #esse metodo é generico do django e estamos sobrescrevendo ele.

        # slug é um tipo de url. Digamos que eu tenha um produto
        # camiseta com o nome "camiseta preta é legal", no slug ficaria parecido com "camiseta-preta-e-legal-123"
        # (o numero seria por ex o id)

        if not self.slug: #O atributo slug não é obrigatorio o usuario preencher, porém, quando fazio, vamos preecher
            #automaticamente usando o metodo slugify do import slugify. Esse metodo edita automaticamente a string
            #passada como parametro de forma que ela tenha a aparencia de um slug.
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)#Antes de sobrescrever um metodo, precisamos chama-lo para não perder
        #o que já existe nele. Até este ponto, não alteramos nada neste metodo

        max_image_size = 800 #variavel com o tamanho de img que queremos

        if self.imagem: #Estamos verificando se a imagem foi enviada lá na tela de admin no produto
            self.resize_image(self.imagem, max_image_size) #se ela foi enviada, chama o metodo acima resize_image


    def __str__ (self):
        return self.nome





class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome #como o nome não será obrigatorio preencher, estamos definindo para que na
    #tela de admin apareça o nome do produto da classe Produto apareça

    class Meta: #Sabemos que os nomes, mesmo que singular, aparecem como plural na tela de admin. Por exemplo,
    #'variacao' apareceria como 'variacaos'. aqui estamos definindo para o singular e o plural para que o django não faça
    #isso automaticamente e mostre nome errado, tipo, 'variacaos'
        verbose_name = 'Variação' #essas duas variaveis são genericas do django
        verbose_name_plural = 'Variações'