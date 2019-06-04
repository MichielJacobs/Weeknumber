import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

	def __init__(self, icon, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)		
		menu = QtWidgets.QMenu(parent)
		refreshAction = menu.addAction("Refresh")
		aboutAction = menu.addAction("About")
		menu.addSeparator()
		exitAction = menu.addAction("Exit")
				
		menu.triggered.connect(self.processtrigger)
		self.setContextMenu(menu)


	def processtrigger(self,q):		
		if q.text () == "Exit":
			sys.exit()

		if q.text() == "About":
			msg = QMessageBox()
			msg.setTextFormat(Qt.RichText)
			msg.setText("This app is created by Michiel Jacobs <br> Visit <a href='https://github.com/MichielJacobs/weeknumber_mj'>my github page</a> for more information.")
			msg.setWindowTitle("About weeknumber")
			msg.exec_()

		if q.text() == "Refresh":
			self.updateTrayIcon()

	def updateTrayIcon(self):
		weeknumber = datetime.datetime.utcnow().isocalendar()[1]
		iconString = str(weeknumber) + ".ico"
		self.setIcon(QtGui.QIcon(iconString))



def main(image):
	app = QtWidgets.QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False) #needed because there is no window by default. Otherwise closing a QMessageBox will result in quiting the app
	w= QtWidgets.QWidget()		
	trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)
	trayIcon.show()
	sys.exit(app.exec_())	



if __name__ == '__main__':
	weeknumber = datetime.datetime.utcnow().isocalendar()[1]
	on=str(weeknumber) + ".ico"
	#on="test1.svg"
	main(on)



