import sys
from desenho import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self) #Lembrando que esse setupUi é um metodo da classe Ui_MainWindow que herdamos.
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem) #Quando clicar no btn 'btnEscolherArquivo', executa
        #a função abrir_imagem
        self.btnRedimensionar.clicked.connect(self.redimensionar) #Quando clicar no btn 'btnRedimensionar', executa a função
        #redimensionar
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):#Este metodo será responsavel por abrir aquela tela para buscar arquivos
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget, #centralwidget é a variavel que corresponde
            #ao elemento da minha tela que vai receber a imagem. Vem da classe 'Ui_MainWindow' do arquivo desenho.
            'Abrir imagem',
            'C:/Users/David/Imagens/',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.inputAbrirArquivo.setText(imagem) #Este 'inputAbrirArquivo' do arquivo de desenho, vai receber o endereço da
        #da pasta onde vamos selecionar a imagem
        self.original_img = QPixmap(imagem)#Essa variavel vai receber o endereço da imagem original e depois ser usada abaixo para armazenar
        #no label do arquivo
        self.labelImg.setPixmap(self.original_img) #label da interface recebendo a imagem que foi armazenada na variavel acima

        self.inputLargura.setText(str(self.original_img.width())) #Estamos escrevendo no meu inputLargura a largura (width) da imagem
        self.inputAltura.setText(str(self.original_img.height())) #Estamos escrevendo no meu inputAltura a altura (height) da imagem

    def redimensionar(self): #metodo que vai redimensionar o tamanho da imagem
        largura = int(self.inputLargura.text()) #Vai receber a largura não da imagem, mas sim do numero (texto) que está no inputLargura
        self.nova_imagem = self.original_img.scaledToWidth(largura) #Essa variavel vai receber a imagem original porém com a nova laragura acima.
        #Esse metodo scaledToWidth, quando vc altera a lagura, ele altera automaticamente a largura pra vc
        self.labelImg.setPixmap(self.nova_imagem) #Estamos inserindo no nosso label a nova imagem alterada
        self.inputLargura.setText(str(self.nova_imagem.width()))  #Estamos escrevendo no meu inputLargura a largura (width) da imagem
        self.inputAltura.setText(str(self.nova_imagem.height()))  #Estamos escrevendo no meu inputLargura a altura (height) da imagem

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,#centralwidget é a variavel que corresponde
            #ao elemento da minha tela que vai receber a imagem. Vem da classe 'Ui_MainWindow' do arquivo desenho.
            'Salvar imagem',
            'C:/Users/David/Desktop/',

        )
        self.nova_imagem.save(imagem, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()