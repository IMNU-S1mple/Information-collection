# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildrenForm2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(ChildrenForm)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(ChildrenForm)
        self.textEdit.setGeometry(QtCore.QRect(40, 30, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(ChildrenForm)
        self.label.setGeometry(QtCore.QRect(40, 10, 231, 16))
        self.label.setObjectName("label")

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
        self.pushButton.setText(_translate("ChildrenForm", "PushButton"))
        self.label.setText(_translate("ChildrenForm", "测试用例:文件->打开->url_list.txt"))
