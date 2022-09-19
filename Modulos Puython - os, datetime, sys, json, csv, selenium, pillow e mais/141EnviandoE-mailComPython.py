from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

#As variaveis de email abaixo estou deixando em branco pois este arquivo vai pro git
meuEmail = '' #este é o email que vai enviar
minhaSenha = '' #senha para logar no gmail
emailDestino = ''

from email.mime.multipart import MIMEMultipart #padrão pra gente enviar email, tipo assunto, pra vai ser enviado e etc
from email.mime.text import MIMEText #Vai receber o corpo do email, nós vamos usar html
from email.mime.image import MIMEImage #vai receber uma img pra gente anexar no email
import smtplib



with open ('template.html', 'r') as html:  #vamos abrir um novo arquivo com o nome de 'template.html'. 'w' é para leitura
    #e escrita. Este arquivo template.html está dentro da propria pasta deste arquivo da aula 140
    template = Template(html.read()) #Vamos usar o Templete para ler e receber o arquivo html
    dataAtual = datetime.now().strftime('%d/%m/%Y') #armazenando a data atual
    corpoMsg = template.safe_substitute(nome='Davidson Marcos', data=dataAtual) #usando o metodo safe_substitute
    #para escrever as variaveis nome e data nos locais onde tiver $nome e $data no arquivo html

msg = MIMEMultipart() #Variavel vai receber a classe MIMEMultipart
msg['from'] = 'Davidson Marcos' #Quem está enviando o email
msg['to'] = emailDestino #pra quem vai o e-mail
msg['subject'] = 'Atenção: Este é um email de teste' #assunto do e-mail


corpo = MIMEText(corpoMsg, 'html')
msg.attach(corpo)

with open('imagem141.jpg', 'rb') as img: #Abrindo uma img. 'rb' é usado para imagens leitura de bytes
    img = MIMEImage(img.read()) #estamos lendo os bytes da imagem e enviando para MIME
    msg.attach(img)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meuEmail, minhaSenha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)








