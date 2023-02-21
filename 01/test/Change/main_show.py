# -*- coding:utf-8 -*-
# Author by Colin
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


from UI.MainForm2  import  Ui_MainWindow

from main import     Third_Ui_Form

from UI.ChildrenForm2 import *
from UI.Subdomain import *



class MyWindow(QMainWindow, Ui_MainWindow):
    dict_ = {
        'pushButton_2': [2, 'first'],
        'pushButton_3': [3, 'second'],
        'pushButton_4': [4, 'third']
    }

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.first = Ui_ChildrenForm()
        self.second = Ui_SubdomainForm()
        self.third = Third_Ui_Form()
        self.setupUi(self)


        # 多个页面的绑定
        for k, v in self.dict_.items():
            form = QWidget()
            # 将各个子页面添加到对应控件form
            eval('self.{}.setupUi(form)'.format(v[1]))
            # 在stackedWidget添加子控件form
            self.stackedWidget.addWidget(form)
            # 将按钮连接同一个槽函数
            eval('self.{}.clicked.connect(self.show_page)'.format(k))


    # 展示index的页面
    def show_page(self):
        index = self.dict_[self.sender().objectName()][0]
        print(index)
        self.stackedWidget.setCurrentIndex(index)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec())