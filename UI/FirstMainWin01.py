# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstMainWin01.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(450, 220, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 100, 54, 12))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(290, 330, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 160, 54, 12))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 23))
        self.menubar.setObjectName("menubar")
        self.menuhello = QtWidgets.QMenu(self.menubar)
        self.menuhello.setObjectName("menuhello")
        self.menuhello2 = QtWidgets.QMenu(self.menubar)
        self.menuhello2.setObjectName("menuhello2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        self.actionxinjian.setObjectName("actionxinjian")
        self.actionguanbi = QtWidgets.QAction(MainWindow)
        self.actionguanbi.setObjectName("actionguanbi")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menuhello.addAction(self.fileOpenAction)
        self.menuhello.addAction(self.actionxinjian)
        self.menuhello.addAction(self.actionguanbi)
        self.menubar.addAction(self.menuhello.menuAction())
        self.menubar.addAction(self.menuhello2.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWindow)
        self.checkBox.clicked['bool'].connect(self.label.setEnabled)
        self.checkBox.clicked['bool'].connect(self.label_2.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_12.setText(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.menuhello.setTitle(_translate("MainWindow", "??????(F)"))
        self.menuhello2.setTitle(_translate("MainWindow", "??????(E)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.fileOpenAction.setText(_translate("MainWindow", "??????"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionxinjian.setText(_translate("MainWindow", "??????"))
        self.actionxinjian.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionguanbi.setText(_translate("MainWindow", "??????"))
        self.actionguanbi.setShortcut(_translate("MainWindow", "Alt+C"))
        self.addWinAction.setText(_translate("MainWindow", "????????????"))
        self.addWinAction.setToolTip(_translate("MainWindow", "????????????"))
