from ui_mainwindow import Ui_TestDialog
from PyQt4.QtGui import QApplication, QDialog
import sys


class TestDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		mainWindow = Ui_TestDialog()
		mainWindow.setupUi(self)
		mainWindow.testwidget.testMethod()
		mainWindow.testwidget.setText("'Ello, govna!")

app = QApplication(sys.argv)
test = TestDialog()
test.show()
sys.exit(app.exec_())