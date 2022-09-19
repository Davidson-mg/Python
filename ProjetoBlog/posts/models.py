from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone

from PIL import Image #estes dois imports abaixo, têm relação com o processo de definir tamanho de uma img de um post
from django.conf import settings #precisamos importa o settings pq precisamos do media_root dele, que é a variavel
#definida para o caminho das imgs
import os

class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título') #Esse 'verbose_name' serve apenas para
    #exibir um nome diferente quando essa variavel 'titulo_post' for exibida em algum lugar, seja na tela de admin
    #do django ou em qualquer pagina do site
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteudo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.CASCADE,
                                       blank=True, null=True, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado ')

    def __str__(self):
        return self.titulo_post

    def save(self, *args, **kwargs): #esse metodo é generico do django e estamos sobrescrevendo ele.

        super(Post, self).save(*args, **kwargs) #Antes de sobrescrever um metodo, precisamos chama-lo para não perder
        #o que já existe nele. Até este ponto, não alteramos nada neste metodo

        self.redefinir_imagem(self.imagem_post, 800) #lembrandoo que imagem_post é um atributo da classe Post



    @staticmethod #este metodo não vai mecher em nada relacionado a classe, por isso estamos defindo como metodo estatico
    def redefinir_imagem(nome_imagem, nova_largura): #este metodo vai receber o nome da imagem e uma nova largura

        img_path = os.path.join(settings.MEDIA_ROOT, nome_imagem)#estamos pegando o caminho completo da imagem
        img = Image.open(img_path) #estamos armazenando o obj de imagem na variavel img
        altura, largura = img.size #estamos armazenado a altura e lergura via metodo size da classe Image

        nova_altura = (nova_largura * altura) / largura

        nova_imagem  = img.resize((nova_largura, nova_altura), Image.ANTIALIAS) #Salvando a nova largura e altura

        if largura <= nova_largura: #caso o tamanho da img que estamos inserindo seja menor ou igual ao tamanho que
            #quero reduzir, ele fecha o processo. Além disso, esse if impede a img seja salva novamente toda vez que vc
            #editar e salvar o post,mesmo que seja para modificar algo que não tenha relação com a img,
            img.close()
            return

        nova_imagem.save(
            img_path, #estamos reescrevendo a imagem o caminho iriginal
            optimiza=True,
            quality=60
        )
        nova_imagem.close()
