from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import Remover
import cv2

class MainWidget(QMainWindow):

    def __init__(self, remover: Remover.Remover):
        super().__init__()
        self.remover = remover
        self.title = 'Wycinanie ramek'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.fileName = None
        self.imageDirectory = None
        #-------------------WIDGET COMPONENTS------------------
        self.chooseButton = None
        self.imagePixMap = None
        self.image = None
        #------------------------------------------------------
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.chooseButton = QPushButton('wybierz plik', self)
        self.chooseButton.setToolTip('This is an example button')
        self.chooseButton.move(10, 10)
        self.chooseButton.clicked.connect(self.openFileNameDialog)

        self.image = QLabel(self)
        self.image.resize(600, 400)
        self.image.move(10, 20 + self.chooseButton.height())
        self.imagePixMap = QPixmap(None)
        self.imagePixMap = self.imagePixMap.scaled(600, 400)
        self.image.setPixmap(self.imagePixMap)
        self.image.setMinimumSize(1, 1)

        #self.image.clear()

        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()

        self.show()

    @pyqtSlot()
    def openFileNameDialog(self):
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "PDF (*.pdf)", options=options)
        fileName, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "PDF (*.pdf)")
        if fileName:
            #self.image.clear()                                              #????
            self.fileName = fileName                                        #.pdf
            print("PDF: " + self.fileName)
            self.imageDirectory = self.remover.returnImage(self.fileName)   #.jpg
            print("PNG: " + self.imageDirectory)                            #zwraca scierzke png poprawnie
            self.imagePixMap = QPixmap(self.imageDirectory)
            self.imagePixMap = self.imagePixMap.scaled(600, 400)
            self.image.setPixmap(self.imagePixMap)

            self.remover.remove(self.imageDirectory)


    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


