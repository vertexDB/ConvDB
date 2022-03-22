import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


class convDB(QtWidgets.QMainWindow):
    def __init__(self):
        super(convDB, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Перевод валют')
        self.setWindowIcon(QIcon('conv.png'))

        self.ui.input_str.setPlaceholderText('Валюта:')
        self.ui.input_num.setPlaceholderText('Число:')
        self.ui.output_str.setPlaceholderText('Валюта:')
        self.ui.output_num.setPlaceholderText('Число:')
        self.ui.pushButton.clicked.connect(self.in_conv)

    def in_conv(self):
        global input_str
        global output_str
        global input_num
        
        input_str = self.ui.input_str.text() + '+'
        output_str = self.ui.output_str.text()
        input_num = self.ui.input_num.text() + '+'

        self.link_parser()
        
    def link_parser(self):
        global convert
        
        link = 'https://www.google.ru/search?q=' + input_num + input_str + output_str
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        full_page = requests.get(link, headers=headers)
        soup = BeautifulSoup(full_page.content, "html.parser")
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        self.ou_conv()
    
    
    def ou_conv(self):
        output_num = convert[0].text
        self.ui.output_num.setText(str(output_num))

        

app = QtWidgets.QApplication([])
application = convDB()
application.show()

sys.exit(app.exec())