from PyQt4 import QtGui
import sys

import labelTool

class LabelTool(QtGui.QMainWindow, labelTool.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LabelTool, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    tool = LabelTool()
    tool.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
