# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labelTool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(816, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_2.addWidget(self.checkBox_2, 3, 2, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 2)
        self.checkBox_1 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.gridLayout_2.addWidget(self.checkBox_1, 2, 2, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 10, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 9, 0, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setMaximumSize(QtCore.QSize(1671, 16777215))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_2.addWidget(self.graphicsView, 0, 1, 17, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_2.addWidget(self.pushButton_5, 11, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_2.addWidget(self.checkBox_3, 4, 2, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_2.addWidget(self.checkBox_4, 5, 2, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_2.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_2.addWidget(self.pushButton_7, 6, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 7, 0, 1, 1)
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setMaximumSize(QtCore.QSize(167, 16777215))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout_2.addWidget(self.listWidget_2, 12, 2, 5, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 11, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Open_dir = QtGui.QAction(MainWindow)
        self.action_Open_dir.setObjectName(_fromUtf8("action_Open_dir"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Create_BBox = QtGui.QAction(MainWindow)
        self.action_Create_BBox.setObjectName(_fromUtf8("action_Create_BBox"))
        self.action_Delete_BBox = QtGui.QAction(MainWindow)
        self.action_Delete_BBox.setObjectName(_fromUtf8("action_Delete_BBox"))
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Open_dir)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Create_BBox)
        self.menu_Edit.addAction(self.action_Delete_BBox)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Labeling Tool", None))
        self.checkBox_2.setText(_translate("MainWindow", "Pedestrian", None))
        self.label_2.setText(_translate("MainWindow", "Labels", None))
        self.checkBox_1.setText(_translate("MainWindow", "Vehicle", None))
        self.pushButton_3.setText(_translate("MainWindow", "Prev", None))
        self.pushButton_4.setText(_translate("MainWindow", "Save", None))
        self.pushButton_5.setText(_translate("MainWindow", "Next", None))
        self.pushButton_2.setText(_translate("MainWindow", "Open Dir", None))
        self.pushButton.setText(_translate("MainWindow", "Open", None))
        self.checkBox_3.setText(_translate("MainWindow", "Motorcycle", None))
        self.checkBox_4.setText(_translate("MainWindow", "Bycicle", None))
        self.pushButton_6.setText(_translate("MainWindow", "Create Box", None))
        self.pushButton_7.setText(_translate("MainWindow", "Delete Box", None))
        self.label.setText(_translate("MainWindow", "File list", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Open_dir.setText(_translate("MainWindow", "&Open dir", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_Create_BBox.setText(_translate("MainWindow", "&Create BBox", None))
        self.action_Delete_BBox.setText(_translate("MainWindow", "&Delete BBox", None))
        self.action_Save.setText(_translate("MainWindow", "&Save", None))

