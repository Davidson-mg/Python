from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView, View
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario #Classe FormComentario do arquivo forms do app comentarios
from comentarios.forms import Comentario
from django.contrib import messages

class PostIndex(ListView): #repare que estamos herdando da classe importada ListView e a classe abaixo herda da nossa
    #casse PostIndex. Essa classe já implementa pra gente algumas coisas relacionadas a lista de objetos
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'


    def get_queryset(self):
        qs = super().get_queryset() #estamos pegando da nossa classe pai (ListView) com o super, o metodo get_queryset
        #que está relacionado aos obj, neste caso, aos posts

        qs = qs.select_related('categoria_post') #Nosso codigo funcionario sem o categoria_post, todavia, sem ele
        #Ao chamarmos a categoria no html, ele faria varias consultas internas desnecessarias no BD para mostrar a
        # categiria. O categoria_post vai apenas reduzir essas consultas, otimizando nosso codigo

        qs = qs.order_by('-id').filter(publicado_post=True) #estamos ordenando de forma decrescente pelo id e mostrando
        #apenas os posts que forma marcados como publicados na tela de admin

        qs = qs.annotate( #aqui vamos usar uma variavel para receber a contagem de comentarios e em seguida usar
            #essa variavel no template index no local onde exibe o nº de comentarios
            numero_comentarios=Count( #numero_comentarios é um campo que estamos criando que vai receber uma consulta
                Case( #esse case vai funcionar como if. Se o comentarios está publicado, conta ele
                    When(comentario__publicado_comentario=True, then=1) #when é quando comentario publicado, soma 1
                )
            )
        )

        return qs


class PostBusca(PostIndex):
    pass

class PostCategoria(PostIndex):
    pass

class PostDetalhes(View):
    template_name = 'posts/post_detalhes.html'

    def setup(self, request, *args, **kwargs): #esse metodo é da classe view e estamos sobrescrevendo ele, inserindo
        #os elementos da nossa pagina post, neste caso, post, comentarios e o formulario

        super().setup(request, *args, **kwargs)#Antes de sobrescrever um metodo, precisamos chama-lo para não perder
        #o que já existe nele. Até este ponto, não alteramos nada neste metodo

        #Daqui para baixo no metodo setup, teoricamente deveria estar dentro do metodo get mais abaixo, e funcionaria
        # até certo ponto. Nós teriamos problemas na hora de enviar um comentario, pois retornaria um erro dizendo que
        # PostDetalhes não retornou um http response OBJ, retornando None na verdade.

        pk = self.kwargs.get('pk') #estamos armazenando a PK do post em questão, que vai ser usada abaixo dentro do
        #dicionario contexto em 'post'

        post = get_object_or_404(Post, pk=pk, publicado_post=True) #estamos pegando o obj post. Apenas os que foram
        #marcados para serem publicados

        self.contexto = { #estamos armazenando o nosso contexto, que é formado de um post, comentarios e o form

            #'post': Post.objects.get(pk = pk), Essa linha faz o mesmo que a linha get_object_or_404 acima da variavel
            # contexto e posteriormente utilizada abaixo em 'post'. Colocamos fora da variavel contexto para poder ser
            # reutilizada pelos demais elementos, por exemplo em comentarios. A a diferença é que com get_object_or_404
            # nós acrescentamos o recurso de erro, descartando a nessecidade de um try. Por isso comentamos aqui.
            # O get_object_or_404 é melhor quando se trata de um unico obj

            'post': post, #lembrando que get_object_or_404 precisa de um import
            'comentarios': Comentario.objects.filter(post_comentario=post, publicado_comentario=True), #Estamos
            # selecionando apenas o comenterios que estão selecionado para serem publicados e que recebem o id do post
            # atual
            'form': FormComentario(request.POST or None),#Caso a pessoa clique em enviar o formulario, mas o formulario
            # não é enviado por algum erro, ele não perde o que foi digitado e se enviar sem digitar nada, estará vazio

        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):

        form = self.contexto['form']

        if not form.is_valid(): #validando os elementos do formulario. Se tiver algo erro, retorna pra pagina
            #aqui mesmo
            return render(request, self.template_name, self.contexto)

        comentario = form.save(commit=False)

        # Um comentario pode ser associado a um usuario admin. Porém, um visitante comum do site
        # não é um usuarioa dmin. Por este motivo, abaixo vamos validar que, caso a pessoa que efetuar
        # o comentario não esteja logada (não é usuario admin), não dê erro exigindo informar um usuario.
        # Lembrando que definimos no models que o compo usuario_comentario não é obrigatorio preencher

        if request.user.is_authenticated:
            comentario.usuario_comentario = request.user

        comentario.post_comentario = self.contexto['post']
        comentario.save()
        messages.success(request, 'Seu comentário foi enviado para revisão e será postado somente se for um elogio. Não aceitamos criticas nem mesmo construtivas.')
        return redirect('post_detalhes', pk=self.kwargs.get('pk')) #estamos recarregando a mesma pagina do post atual





# class PostDetalhes(UpdateView): #Repare que essa classe é a unica que não herda das classe anteriores, herdando da
#     #classe importada UpdateView.
#     template_name = 'posts/post_detalhes.html'
#     model = Post
#     form_class = FormComentario #essa classe FormComentario criamos manualmente no arquivo form no app comentarios.
#     #Estamos pegando os atributos de comentarios do tipo form
#
#     context_object_name = 'post' #Estamos nomeando o contexto. Aqui será post e não posts como anteriormente, pois
#     #estamos dentro da pagina do post, logo passa a ser um post e não posts
#
#     def get_context_data(self, **kwargs):#para fazer com que os comentarios sejam exibidos na pagina, vamos precisar
#     #sobreecrever este metodo. Isso por conta dos comentarios que existem mas estão selecionados para não aparecer
#
#         contexto = super().get_context_data(**kwargs) #antes de sobreescrever, estamos armazendo o que já existe
#         #lemrabrando que o context é o post que já invetamos na pagina, por exemplo {{ posts.titulo_post }}
#
#         post = self.get_object() #estou obtendo o post que estamos atualmente
#
#         comentarios = Comentario.objects.filter(publicado_comentario=True, post_comentario=post.id) #Estamos selecionando
#         #apenas o comenterios que estão selecionado para serem publicados e que recebem o id do post atual
#
#         contexto['comentarios'] = comentarios #enjetamos o novo contexto que é referente aos comentarios
#
#         return contexto
#
#
#     def form_valid(self, form): #Neste metodo pegar os valores inseridos no formulario e validar
#         post = self.get_object()
#         comentario = Comentario(**form.cleaned_data)
#         comentario.post_comentario = post #lembrando que 'post_comentario' é uma FK que associa o comentario ao post.
#         #Estamo armazendo na variavel 'post_comentario' o id do post em que estamos
#
#         #Um comentario pode ser associado a um usuario admin. Porém, um visitante comum do site
#         #não é um usuarioa dmin. Por este motivo, abaixo vamos validar que, caso a pessoa que efetuar
#         #o comentario não esteja logada (não é usuario admin), não dê erro exigindo informar um usuario.
#         #Lembrando que definimos no models que o compo usuario_comentario não é obrigatorio preencher
#
#
#         if self.request.user.is_authenticated: #verificando se o usuarioe está autenticado
#             comentario.usuario_comentario = self.request.user #se estiver logado, pega o valor do usuario logado
#
#         comentario.save()
#         messages.success(self.request,'Comentário enviado com sucesso.')
#         return redirect('post_detalhes', pk=post.id) #estamos recarregando a mesma pagina do post atual

class PostDetalhes(UpdateView): #Repare que essa classe é a unica que não herda das classe anteriores, herdando da
    #classe importada UpdateView
    pass

