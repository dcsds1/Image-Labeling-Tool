from PyQt4 import QtGui, QtCore
import sys

import labelTool


class LabelTool(QtGui.QMainWindow, labelTool.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LabelTool, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.open_file)

    def open_file(self):
        print "Opening a file...I'm trying very hard..."
        file_name = QtGui.QFileDialog.getOpenFileName(
            self,
            "Open File",
            QtCore.QDir.currentPath())
        print file_name
        if file_name:
            image = QtGui.QImage(file_name)

            pixmap = QtGui.QPixmap(file_name)
            pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            pic = QtGui.QLabel(self.paintHere)
            pic.setPixmap(pixmap)
            pic.show()
        self.scaleFactor = 1.0

def main():
    app = QtGui.QApplication(sys.argv)
    tool = LabelTool()
    tool.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
