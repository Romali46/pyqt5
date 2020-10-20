from PyQt5.QtCore import *
from  PyQt5.QtWidgets import *
import sys
def bio():
    app = QApplication(sys.argv)
    window = QWidget()
    sample = QGridLayout()

    h = QHBoxLayout()
    drop = QComboBox()

    asa1 = QLabel("style")
    drop.addItem("Fusion")

    c1 = QCheckBox("Use style's standart pallete")
    c1.setChecked(True)
    c2 = QCheckBox("Disable Widgets")

    h.addWidget(asa1)
    h.addWidget(drop)

    sample.addLayout(h,1,1)
    sample.addWidget(c1,1,2,1,2)
    sample.addWidget(c2,1,4)

    bagian1 = QGroupBox("Group 1")
    bagian2 = QGroupBox("Group 2")
    bagian3 = QGroupBox("Group 3")
    bagian3.setCheckable(True)
    bagian3.setChecked(True)

    sample.addWidget(bagian1,2,1)
    sample.addWidget(bagian2,2,3)
    sample.addWidget(bagian3,10,3)

    #GROUP 1 
    g= QGroupBox()
    sample.addWidget(g,4,1,5,2)
    vbox = QVBoxLayout()
    g.setLayout(vbox)

    B1 = QRadioButton("Radio Button 1")
    B2 = QRadioButton("Radio Button 2")
    B3 = QRadioButton("Radio Button 3")
    sCBox = QCheckBox("Tri-State Check Box")
    sCBox.setTristate(True)
    sCBox.setCheckState(1)

    vbox.addWidget(B1)
    vbox.addWidget(B2)
    vbox.addWidget(B3)
    vbox.addWidget(sCBox)

    #GROUP 2 
    g2 = QGroupBox()
    sample.addWidget(g2,4,3,5,2)
    vbox2 = QVBoxLayout()
    g2.setLayout(vbox2)

    BD1 = QPushButton("Default Push Button")
    BD1.setDefault(True)
    BD2 = QPushButton("Toggle Push Button")
    BD3 = QPushButton("Flat Push Button")
    BD3.setFlat(True)

    vbox2.addWidget(BD1)
    vbox2.addWidget(BD2)
    vbox2.addWidget(BD3)

    #GROUP 3 
    g3 = QGroupBox()
    sample.addWidget(g3,10,3,5,2)
    vbox3 = QVBoxLayout()
    g3.setLayout(vbox3)

    lineEdit = QLineEdit("1234567890")
    lineEdit.setEchoMode(QLineEdit.Password)

    spin = QSpinBox()
    spin.setValue(50)

    date = QDateTimeEdit()
    date.setDate(QDate(2018,9,24))
    date.setTime(QTime(1,56,0,0))
    date.setDisplayFormat(("dd.MM.yyHH:mm"))

    S = QSlider()
    S.setValue(35)
    S.setOrientation(Qt.Horizontal)

    dl = QDial()
    dl.setValue(35)
    sb =QScrollBar()
    sb.setValue(60)

    sb.setOrientation(Qt.Horizontal)

    sample.addWidget(lineEdit,12,3,1,2)
    sample.addWidget(spin,13,3,1,2)
    sample.addWidget(date,14,3,1,2)
    sample.addWidget(S,15,3,1,1)
    sample.addWidget(dl,15,4,2,1)
    sample.addWidget(sb,16,3,1,1)

    bar = QProgressBar()
    bar.setValue(22)
    sample.addWidget(bar,18,1,2,4)

    #layout
    tab = QTabWidget()
    table = QTableWidget()
    table.setRowCount(10)
    table.setColumnCount(10)
    tab.addTab(table,"")
    tab.setTabText(0,"Table")
    textEdit = QTextEdit()
    tab.addTab(textEdit,"")
    tab.setTabText(1,"Text Edit")

    sample.addWidget(tab,10,1,8,2)

    window.setLayout(sample)
    window.setWindowTitle("Styles")
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    bio()
