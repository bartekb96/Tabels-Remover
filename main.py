from PySide2.QtWidgets import QApplication
import sys
import mainWidget
import Remover

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tableRemover = Remover.TableRemover()
    headerRemover = Remover.HeaderRemover()

    mainWidget = mainWidget.MainWidget(tableRemover)

    #sys.exit(app.exec_())
    app.exec_()