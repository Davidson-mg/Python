from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')


    user = auth.authenticate(request,username=usuario, password=senha) #Através do import auth acima, estamos pegando
    #usando o metodo 'authenticate' para verificar se este usuario e senha existem. Se não existe, armazena 'None"

    if not user: #Se não existe o usuario
        messages.error(request, 'Usuário ou senha invalidos') #exibe a msg de aviso. Lembrando que estas messagens vem
        # do html _messages da pasta parciais e por sua vez foi configurado no arquivo settings em 'MESSAGE_TAGS'
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user) #Está fazendo login com o usuario e senha armazenados na variavel user acima
        messages.success(request, 'Login efetuado com sucesso')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def cadastro(request):
    if request.method != 'POST': #Estamos verificando se foi enviado alguma coisa no formulario
        return render(request, 'accounts/cadastro.html') #retorna o formulario original (vazio)

    #Abaixo vamos salvar os dados de cadastro na base de dados do admin do django, mas poderá ser usado tanto
    #para alguem que queira ter acesso de admin no site, quanto para cadastrar usuario comuns mesmo

    nome = request.POST.get('nome') #Estas variaveis vão receber os valores dos campos da tela de fazer cadastro
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2: #caso tenha algum campo vazio
        messages.error(request, 'Nenhum campo pode estar vazio') #exibe a msg de aviso
        return render(request, 'accounts/cadastro.html') #retorna o formulario original (vazio)

    try: #Estamos validando o e-mail.
        validate_email(email) #essa função vem do import validate_email. É do proprio django e já faz a validação pra
        #gente
    except: #ao inves de retornar uma exceção, vamos configurar para retornar apenas a msg
        messages.error(request, 'Email inválido') #exibe a msg de aviso. Lembrando que estas messagens vem do html
        #_messages da pasta parciais e por sua vez foi configurado no arquivo settings em 'MESSAGE_TAGS'
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 4: #Definindo que a senha precisa ser igual ou maior que 4 caracteres

        messages.error(request, 'Senha precisa ter 6 ou mais caracteres')#exibe a msg de aviso. Lembrando que estas
        # messagens vem do html _messages da pasta parciais e por sua vez foi configurado no arquivo settings em
        # 'MESSAGE_TAGS'
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6: #Definindo que o usuario precisa ser igual ou maior que 6 caracteres

        messages.error(request, 'Usúario precisa ter 6 ou mais caracteres')#exibe a msg de aviso. Lembrando que estas
        # messagens vem do html _messages da pasta parciais e por sua vez foi configurado no arquivo settings em
        # 'MESSAGE_TAGS'
        return render(request, 'accounts/cadastro.html')

    if senha != senha2: #verificando se a senha é igual a senha repetida
        messages.error(request, 'Senha diferente')#exibe a msg de aviso. Lembrando que estas
        # messagens vem do html _messages da pasta parciais e por sua vez foi configurado no arquivo settings em
        # 'MESSAGE_TAGS'
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists(): #Estamos verificando se o usuario já existe. Para isso, usamos
        #o import User do django que já faz isso pra gente
        messages.error(request, 'Usuário já existe')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists(): #Estamos verificando se o usuario já existe. Para isso, usamos
        #o import User do python que já faz isso pra gente
        messages.error(request, 'Email já existe')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, "Registrado com sucesso! Faça seu login.") #Se chegar até aqui é pq deu tudo certo, então retorne
    #msg de sucesso

    #Com o import user do django, podemos salvar os dados de cadastro de usuario no django conforme abaixo
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()

    #Depois de salvar, redireciona para a tela de login com o formulario de acesso
    return redirect('login')


#Este parametro vem do import login_required. Se eu acesso a pagina de
#dashboard sem ter efetuado o login, ele não deixa eu acessar e me encaminha pra tela de login
@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato() #Essa classe FormContato criamos no arquivo models.
        return render(request, 'accounts/dashboard.html', {'form': form})#Estamos envia a classe FormContato num dicionario
        #para o arquivo dashboard.html


    #Daqui pra baixo vamos validar o fomulario. Primeiro vamos validar usando
    #uma validação propria do Django

    form = FormContato(request.POST, request.FILES) # #Essa classe FormContato criamos no arquivo models.
    # Esse request.POST é o que vem ao enviarmos o fomulario, ou seja os valores preenchidos nos campos. O request.Files só
    # usamos quando temos algum campo de imagem

    if not form.is_valid(): #Esse metodo do django vai fazer uma validação de todos os campos pra gente. Caso não seja
        #valido, ele executa o que está abaixo
        messages.error(request, 'Erro ao enviar o formulário')#exibe a msg de aviso. Lembrando que estas messagens
        #vem do html _messages da pasta parciais e por sua vez foi configurado no arquivo settings em 'MESSAGE_TAGS'
        form.save()
        return render(request, 'accounts/dashboard.html', {'form': form})


    #Daqui pra baixo é opcional. Fizemos uma validação sem Django mais como exemplo mesmo

    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Descrição precisa ter mais que 5 caracteres')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form':form})


    #depois que passou das validações

    form.save() #salva o formulario
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    return redirect('dashboard') #retorna para a pagina do dashboard