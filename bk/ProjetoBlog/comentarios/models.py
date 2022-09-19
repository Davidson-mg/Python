from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE) #Quando um post for apagado, deve eliminar
    #todos os comentarios relacionados a ele, por isso usamos o 'on_delete=models.CASCADE'
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)#Digamos que um
    # funcionario que postava artigos no blog tenha sido demitido, não queremos que os artigos dele sejam apagados.
    # Por isso usamos on_delete=models.DO_NOTHING
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario
