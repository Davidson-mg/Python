from django.db import models
from django.utils import timezone

#aqui vamos colocar as representações de classes de nossas tabelas

class Categoria (models.Model): #tablea categoria
    nome = models.CharField(max_length=255)
    def __str__(self): #representando categoria pelo nome. Pode ver o resultado disso no acesso /admin e em contatos
        #Deve configurar também no arquivo admin.py
        return self.nome

class Contato(models.Model): #tabela contato
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, )#Com o atributo blanck estmaos dizendo que é opcional
    telefone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now) #Esse time zone precisa do importe timezone acima coloca data
    #atual automaticamente
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) #Esse on_delete serve para não apagar os dados
    #que possuem relação com categoria
    mostrar = models.BooleanField(default=True) #um atributo que será do tipo marca/desmarca. Vamos usa-lo na tela de
    #admin do django. Ao desrma-lo, ele deixa de mostrar o contato na pagina do site. Veja tb sobre o if que adicionamos
    #pagina index que, em caso de True, mostre o conteudo
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d') #Estamos gerando um atributo que será responsavel
    #por armazenar imagens. Com essa data no final, estamos dizendo que para cada vez que fizermos um upload de uma nova
    #imagem, terá uma pasta nova com a data do novo upload

    def __str__(self):
        return self.nome


#Sempre que fizer alguma alteração de BD, digite os comandos abaixo na sequecia no terminal:
# python manage.py makemigrations
# python manage.py migrate


#Comando para criar usuario na tela de admina do Django
#python manage.py createsuperuser




