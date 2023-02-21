import pathlib
import sys, path

from PyQt5.QtGui import QIcon, QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QStackedLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QEventLoop, QTimer
from UI.MainForm2 import *
from UI.ChildrenForm2 import *
from UI.Subdomain import *

from Function import ICMP_Scan01, Check_CDN

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QStackedLayout
import sys
from UI.ChildrenForm2 import *
from UI.Subdomain import *
from UI.MainForm2 import *




class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("QStackedLayout 例子")
        self.resize(300, 270)
        # 创建堆叠布局

        self.btnPress1 = QPushButton("FormA")
        self.btnPress2 = QPushButton("FormB")

        self.form1 = ChildrenForm()
        self.form2 = SubdomainForm()

        widget = QWidget()
        self.stacked_layout = QStackedLayout()
        widget.setLayout(self.stacked_layout)

        self.stacked_layout.addWidget(self.form1)
        self.stacked_layout.addWidget(self.form2)

        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)

        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.stacked_layout.setCurrentIndex(0)

    def btnPress2_Clicked(self):
        self.stacked_layout.setCurrentIndex(1)

class ChildrenForm(QWidget, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


class SubdomainForm(QWidget, Ui_SubdomainForm):
    def __init__(self):
        super(SubdomainForm, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
