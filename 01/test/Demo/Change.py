from PyQt5.QtWidgets import *

import sys

from UI.ChildrenForm2 import *

class MainPanel(QWidget):
    def __init__(self):
        super(MainPanel, self).__init__()
        self.resize(400, 400)
        mainPanel_layout = QHBoxLayout()

        button_layout = QVBoxLayout()
        select_Panel1_button = QPushButton("panel1")
        select_Panel2_button = QPushButton("panel2")
        select_Panel3_button = QPushButton("panel3")
        select_Panel4_button = QPushButton("panel4")

        button_layout.addWidget(select_Panel1_button)
        button_layout.addWidget(select_Panel2_button)
        button_layout.addWidget(select_Panel3_button)
        button_layout.addWidget(select_Panel4_button)

        one = onePanel()
        two = twoPanel()
        three = threePanel()
        four = fourPanel()

        qls = QStackedLayout()
        a = qls.addWidget(one)
        # print(a)
        b = qls.addWidget(two)
        # print(b)
        c = qls.addWidget(three)
        # print(c)
        d = qls.addWidget(four)

        mainPanel_layout.addLayout(button_layout)
        mainPanel_layout.addLayout(qls)

        select_Panel1_button.clicked.connect(lambda: self.buttonIsClicked(select_Panel1_button, qls))
        select_Panel2_button.clicked.connect(lambda: self.buttonIsClicked(select_Panel2_button, qls))
        select_Panel3_button.clicked.connect(lambda: self.buttonIsClicked(select_Panel3_button, qls))
        select_Panel4_button.clicked.connect(lambda: self.buttonIsClicked(select_Panel4_button, qls))

        self.setLayout(mainPanel_layout)

    def buttonIsClicked(self, button, qls):
        dic = {
            "panel1": 0,
            "panel2": 1,
            "panel3": 2,
            "panel4": 3
        }
        index = dic[button.text()]
        qls.setCurrentIndex(index)


class onePanel(QWidget):
    def __init__(self):
        super(onePanel, self).__init__()
        self.setStyleSheet('''QWidget{background-color:#66CCFF;}''')

        onePanel_layout = QHBoxLayout()
        qlabel = QLabel("这是界面1")
        onePanel_layout.addWidget(qlabel)

        self.setLayout(onePanel_layout)


class twoPanel(QWidget):
    def __init__(self):
        super(twoPanel, self).__init__()
        self.setStyleSheet('''QWidget{background-color:#66ffcc;}''')

        twoPanel_layout = QHBoxLayout()
        qlabel = QLabel("这是界面2")
        twoPanel_layout.addWidget(qlabel)

        self.setLayout(twoPanel_layout)

class threePanel(QWidget):
    def __init__(self):
        super(threePanel, self).__init__()
        self.setStyleSheet('''QWidget{background-color:#ee0000;}''')

        threePanel_layout = QHBoxLayout()
        qlabel = QLabel("这是界面3")
        threePanel_layout.addWidget(qlabel)

        self.setLayout(threePanel_layout)

class fourPanel(QWidget):
    def __init__(self):
        super(fourPanel, self).__init__()
        self.setStyleSheet('''QWidget{background-color:#ee0200;}''')

        fourPanel_layout = QHBoxLayout()
        qlabel = QLabel("这是界面4")
        fourPanel_layout.addWidget(qlabel)

        self.setLayout(fourPanel_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainPanel()
    main.show()
    sys.exit(app.exec_())