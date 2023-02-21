import pathlib
import sys,path

from PyQt5.QtGui import QIcon, QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QStackedLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QEventLoop, QTimer
from UI.MainForm2 import *
from UI.ChildrenForm2  import *
from UI.Subdomain import *
from UI.Is_lived import *
from UI.Tcp_Is_lived import *
from UI.Port_Scan import *
from UI.Dir_Search import *

from Function import ICMP_Scan01,Check_CDN,Subdomain,TCP_Scan01,Port_Scan,Dirsearch




class MainForm(QMainWindow, Ui_MainWindow):
    dict_ = {
        'pushButton_2': [2, 'child'],
        'pushButton_3': [3, 'domain'],
        'pushButton_4': [4, 'is_ilved'],
        'pushButton_5': [5, 'tcp_is_lived'],
        'pushButton_6': [6, 'port_scan'],
        'pushButton_7': [7, 'dir_search']
    }
    def __init__(self):
        super(MainForm, self).__init__()

        # self.child = children()生成子窗口实例self.child
        self.child = Ui_ChildrenForm()
        self.domain = Ui_SubdomainForm()
        self.is_ilved = Ui_IsLivedForm()
        self.tcp_is_lived = Ui_TCPIsLived()
        self.port_scan = Ui_PortSacnForm()
        self.dir_search = Ui_DirSearchForm()


        self.setupUi(self)
        self.initIco()

        for k, v in self.dict_.items():
            print(k,v)
            form = QWidget()
            # 将各个子页面添加到对应控件form
            eval('self.{}.setupUi(form)'.format(v[1]))
            # 在stackedWidget添加子控件form
            self.stackedWidget.addWidget(form)
            # 将按钮连接同一个槽函数
            eval('self.{}.clicked.connect(self.show_page)'.format(k))



        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        # self.fileCloseAction.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)



        # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
        # self.addWinAction.triggered.connect()




        self.label_2.setText("<A href='https://imnu-s1mple.github.io/'>欢迎访问作者的博客 By:WYQ</a>")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setToolTip('这是一个超链接标签')
        self.label_2.linkActivated.connect(link_clicked)
        self.label_2.setOpenExternalLinks(True)

        # self.pushButton.clicked.connect(self.getTextEdit)

        self.child.pushButton.clicked.connect(self.Check_CDN)
        self.domain.pushButton.clicked.connect(self.SubDomain)
        self.is_ilved.pushButton.clicked.connect(self.Is_Lived)
        self.tcp_is_lived.pushButton.clicked.connect(self.TCP_Is_Lived)
        self.port_scan.pushButton.clicked.connect(self.Port_Scan)
        self.dir_search.pushButton_2.clicked.connect(self.Dir_Search)



        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

        self.pushButton_12.clicked.connect(self.shutDown)

        self.dir_search.pushButton.clicked.connect(self.dirFilename)
        self.dir_search.label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.child.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.is_ilved.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.port_scan.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.domain.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.tcp_is_lived.label.setTextInteractionFlags(Qt.TextSelectableByMouse)




    def show_page(self):
        index = self.dict_[self.sender().objectName()][0]
        self.stackedWidget.setCurrentIndex(index)

    def shutDown(self):
        sys.exit()

    def initIco(self):
        self.setWindowIcon(QIcon('./ico/yellowPeople.ico'))

    # def childShow(self):
    #     # 添加子窗口
    #     self.MaingridLayout.addWidget(self.child)
    #     self.child.show()
    #
    # def domainShow(self):
    #     self.MaingridLayout.addWidget(self.domain)
    #     self.domain.show()



    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", r"C:\Users\wuyanqing\Desktop\Graduation design\code\Exploring activities\01\test\Function", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)

        self.label.setText(file)

        self.child.textEdit.setText(file)

        self.textEdit.setText(file)

    def dirFilename(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开",r"C:\Users\wuyanqing\Desktop\Graduation design\code\Exploring activities\01\test\Function","All Files (*);;Text Files (*.txt)")
        self.dir_search.textEdit_2.setText(file)


    def Check_CDN(self):
        argument = self.child.textEdit.toPlainText()

        if argument :
            # ICMP_Scan01.main(argument)
            Check_CDN.main(argument)

    def SubDomain(self):
        argument01 = self.domain.lineEdit.text()
        argument02 = self.domain.comboBox.currentText()

        if argument01 and argument02:
            # ICMP_Scan01.main(argument)
            # Check_CDN.main(argument)

            Subdomain.bing_search(argument01,argument02)



    def Is_Lived(self):
        argument = self.is_ilved.lineEdit.text()
        if argument:
            ICMP_Scan01.main(argument)

    def TCP_Is_Lived(self):
        argument = self.tcp_is_lived.lineEdit.text()
        if argument:
            TCP_Scan01.is_lived(argument)
    def Port_Scan(self):
        argument01 = self.port_scan.lineEdit.text()
        argument02 = self.port_scan.comboBox.currentText()
        if argument01:
            if argument02=="全端口扫描":
                Port_Scan.main(argument01)
            else:
                Port_Scan.Some_Port_main(argument01)
    def Dir_Search(self):
        argument01 = self.dir_search.textEdit.toPlainText()
        argument02 = self.dir_search.textEdit_2.toPlainText()
        if argument01 and argument02:
            Dirsearch.Scan(argument01,argument02)



    def outputWritten(self, text):
        # self.textEdit.clear()
        cursor = self.textEdit_2.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit_2.setTextCursor(cursor)
        self.textEdit_2.ensureCursorVisible()



# 重定向信号
class EmittingStr(QtCore.QObject):
        textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

        def write(self, text):
            self.textWritten.emit(str(text))
            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()
        



def link_clicked():
    print("当鼠标点击label-4标签时，触发事件。")


class ChildrenForm(QWidget,Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)

class SubdomainForm(QWidget,Ui_SubdomainForm):
    def __init__(self):
        super(SubdomainForm,self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.setWindowTitle("居家旅行，渗透必备")
    win.show()
    sys.exit(app.exec_())

