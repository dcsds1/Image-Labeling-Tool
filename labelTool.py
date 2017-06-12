#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os

__appname__ = 'labelTool'

#def have_qstring():
#    '''p3/qt5 get rid of QString wrapper as py3 has native unicode str type'''
#    return not (sys.version_info.major >= 3 or QT_VERSION_STR.startswith('5.'))
#
#class WindowMixin(object):
#
#    def menu(self, title, actions=None):
#        menu = self.menuBar().addMenu(title)
#        if actions:
#            addActions(menu, actions)
#        return menu

class MainWindow(QWidget):
    def __init__(self, defaultFilename=None, defaultPrefdefClassFile=None):
        super(MainWindow, self).__init__()
        self.setWindowTitle(__appname__)

        # Create a widget for using default label
        useDefautLabelQHBoxLayout = QHBoxLayout()

        self.useDefautLabelCheckbox = QCheckBox(u'Use default label')
        self.useDefautLabelCheckbox.setChecked(False)
        #self.defaultLabelTextLine = QLineEdit()
        useDefautLabelQHBoxLayout.addWidget(self.useDefautLabelCheckbox)
        #useDefautLabelQHBoxLayout.addWidget(self.defaultLabelTextLine)
        #useDefautLabelContainer = QWidget()
        #useDefautLabelContainer.setLayout(useDefautLabelQHBoxLayout)
        self.setLayout(useDefautLabelQHBoxLayout)


def get_main_app(argv=[]):
    """
    Standard boilerplate Qt application code.
    Do everything but app.exec_() -- so that we can test the application in one thread
    """
    app = QApplication(argv)
    app.setApplicationName(__appname__)
    #app.setWindowIcon(newIcon("app"))

    # argv[1]: IMAGE_PATH
    # argv[2]: PRE-DEFINED CLASS FILE
    win = MainWindow(argv[1] if len(argv) >= 2 else None,
                     argv[2] if len(argv) >= 3 else os.path.join('data', 'predefined_classes.txt'))
    win.show()
    return app, win


def main(argv=[]):
    '''construct main app and run it'''
    app, _win = get_main_app(argv)
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
