from django import forms
from django.contrib.auth.models import User
from . import models


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',) #Estamos excluindo este campo pq eles está sendo utilizado no models e não queremos
        #que o usuario tenha a opção de selecionar usuario quando tiver cadastrando.


class UserForm(forms.ModelForm):

    password = forms.CharField(
        required=False, #Dizendo que o campo de senha não é requerido para não ficar obrigando o usuario a digitar nova
        #senha sempre que atualizar seu cadastro
        widget=forms.PasswordInput(), #Impede que fique aparecendo um codigo maluco no campo de senha em caso de usuario
        #que já possuem um cadastro, e por isso possuem uma senha mas estão atualizando o cadastro
        label='Senha', #defindo que no html no campo de senha, ao inves de aparecer password aparecça senha
    )

    password2 = forms.CharField(
        required=False, #Dizendo que o campo de senha não é requerido para não ficar obrigando o usuario a digitar nova
        #senha sempre que atualizar seu cadastro
        widget=forms.PasswordInput(), #Impede que fique aparecendo um codigo maluco no campo de senha em caso de usuario
        #que já possuem um cadastro, e por isso possuem uma senha mas estão atualizando o cadastro
        label='Confirmação senha' #defindo que no html no campo de senha, ao inves de aparecer password aparecça senha
    )

    #Nós precisamos checar se o usuario e o e-mail preenchidos no formulario de criar perfil já existe.
    #Existe duas formas de fazer essa checagem. A primeira é esperar o usuario enviar o formulario com e-mail e usuario
    #e simplesmente checar se já existem na base de dados. Outra forma é atualizar
    #Aqui vamos optar pela forma de atualizar
    #Em nosso projeto, teremos uma unica tela para login e para cadastro/atualizar cadastro. Se o usuario estiver logado
    #A tela de login fica a esquerda e a de cadastro/atualizar fica a direita.
    #Se o cadastro do cliente já existe, ele consegue atualizar algum informação de seu cadastro no formulario
    #a direita. Além disso, se o cadastro já existe, ele não é obrigado a preencher nova senha



    #Se o usuario estiver logado, vamos pegar os dados desse usuario logado
    def __init__(self, usuario=None, *args, **kwargs): #isso não existe no django, nós que estamos criando. Se trata
    #de um construtor onde estamos criando um atributo que pertence a nossa classe UserForm que é a variavel
    #usuario=none e 'puxando' qualquer outra variavel vinda de ModelForm (herança) que são os *args e **kwargs

        super().__init__(*args, **kwargs) #Lembrando que args e kwargs são qualquer coisa. O super no caso está
    #pegando os atributos que vem como herança da classe pai, que neste caso é a classe ModelForm

        self.usuario = usuario # Definindo o atributo usuario pois ele é especifico desta classe UserForm e não de
        #herança

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password',
                  'password2', 'email')

    def clean(self, *args, **kwargs):  # Aqui vamos validar os campos do formulario
        data = self.data  # este data pega os dados do formulario 'cru'
        cleaned = self.cleaned_data  # cleaned pega os dados limpos do formulario
        validation_error_msgs = {}  # criamos essa variavel do tipo dicionario vazio que vai receber nossas exceções
        # abaixo

        usuario_data = cleaned.get('username')  # estamos pegando o usuario que a pessoa digitou no input no html
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()  # Armazenando na variavel usuario_db se o
        # usuario_data existe. Estamos filtrando no obj de Usuarios todos usuarios com este nome. Se não existe
        # armazena none
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Usuário já existe'  # variavei que recebem as msgs de erros
        error_msg_email_exists = 'E-mail já existe'
        error_msg_password_match = 'As duas senha não conferem'
        error_msg_password_short = 'Sua senha precisa de pelo menos 6 caracteres'
        erro_msg_required_field = 'Este campo é obrigatorio.'


        # Em nosso projeto, teremos uma unica tela para login e para cadastro/atualizar cadastro. Se o usuario estiver logado
        # A tela de login fica a esquerda e a de cadastro/atualizar fica a direita.
        # Se o cadastro do cliente já existe, ele consegue atualizar algum informação de seu cadastro no formulario
        # a direita. Além disso, se o cadastro já existe, ele não é obrigado a preencher nova senha


        #usuario logados: atualização
        if self.usuario:
            # validation_error_msgs['username'] = 'Errouuuuuuuuuu'

            if usuario_db:  # Checando se o usuario existe
                if usuario_data != usuario_db.username: #se usuario digitado pelo usuario for diferente do usuario selecionado
                #na base de dados
                    validation_error_msgs['username'] = error_msg_user_exists #Armazenando um erro relacionado ao
                    #usuario com a msg armazenada na variavel error_msg_user_exists

            if email_db:
                if email_data != email_db.email: #Verificando se o e-mail foi enviado
                    validation_error_msgs['email'] = error_msg_email_exists


            if password_data: #Se a senha foi enviada
                if password_data != password2_data: #verificando se a senha 1 é igual a senha 2
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6: #verificano se a senha digitada é menor que 6 caracteres
                    validation_error_msgs['password'] = error_msg_password_short


        #usuarios não logados: cadastro
        else:
            if usuario_db:  # se usuario digitado pelo usuario for diferente do usuario selecionado
                # na base de dados
                validation_error_msgs['username'] = error_msg_user_exists  # Armazenando um erro relacionado ao
            # usuario com a msg armazenada na variavel error_msg_user_exists

            if email_db:  # Verificando se o e-mail foi enviado
                validation_error_msgs['email'] = error_msg_email_exists

            if not password_data:
                validation_error_msgs['password'] = erro_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = erro_msg_required_field

            if password_data != password2_data:  # verificando se a senha 1 é igual a senha 2
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

            if len(password_data) < 6:  # verificano se a senha digitada é menor que 6 caracteres
                validation_error_msgs['password'] = error_msg_password_short



        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))
