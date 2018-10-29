import sys  # Operating System interaction module
from PyQt5 import QtWidgets, uic  # GUI management module based on Qt

# Load in memory the associated GUI produced with QtDesigner
# mainwindow.ui is the .ui file created with QtDesigner
Ui_MainWindow, QtBaseClass = uic.loadUiType("mainwindow.ui")


class MainWindow(QtWidgets.QMainWindow):
    # __init__ function
    #
    # Called at instanciation of MainWindow
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # EXAMPLE: Connection to the buttons from the GUI
		# pushButtonUpdateFTStatus is the widget name
		# ft_status_log_in_and_update is the function to call
        self.ui.pushButtonUpdateFTStatus.clicked.connect(self.ft_status_log_in_and_update)  # FT Status tab
    
	def ft_status_log_in_and_update(self):
		# WRITE CODE
		
# main
if __name__ == "__main__":  # Allows to double click on Main.py to launch the GUI
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()		# Display / Refresh window
    sys.exit(app.exec_())	# Clean exit of the application
