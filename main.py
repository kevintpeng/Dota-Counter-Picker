# MAIN FILE
#-----------------------------------------------------
# Run this file to launch the GUI and use the program.

from PyQt4 import QtCore, QtGui
from analyze_data import AnalyzeData
from dota_dumper import DotaDumper
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

class Ui_HeroSelect(object):
    def __init__(self):
        # Will read the list from the text file
        with open("HeroList.txt") as file_list:
            self.hero_list = file_list.readlines()
            self.list_length = len(self.hero_list)
            self.clean_list = []
            self.file_path = "data.csv"
            for i in range(0, self.list_length):
                self.hero_list[i] = self.hero_list[i].replace("\n", "")
            for i in range(0, self.list_length):
                self.clean_list.append(self.hero_list[i].lower().replace(" ", "-").translate(None,"'"))
            # creates objects of the other two classes
            self.analysis = AnalyzeData()
            self.dumper = DotaDumper()
            self.rows = self.analysis.read_table()
            self.values = {}
            for i in range(0, self.analysis.list_length):
                self.values[self.analysis.clean_list[i]] = 0

    # GUI definitions
    def setupUi(self, HeroSelect):
        HeroSelect.setObjectName(_fromUtf8("HeroSelect"))
        HeroSelect.resize(272, 270)
        self.centralwidget = QtGui.QWidget(HeroSelect)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.hero1 = QtGui.QComboBox(self.centralwidget)
        self.hero1.setObjectName(_fromUtf8("hero1"))

        self.verticalLayout.addWidget(self.hero1)
        self.hero2 = QtGui.QComboBox(self.centralwidget)
        self.hero2.setObjectName(_fromUtf8("hero2"))
        self.verticalLayout.addWidget(self.hero2)
        self.hero3 = QtGui.QComboBox(self.centralwidget)
        self.hero3.setObjectName(_fromUtf8("hero3"))
        self.verticalLayout.addWidget(self.hero3)
        self.hero4 = QtGui.QComboBox(self.centralwidget)
        self.hero4.setObjectName(_fromUtf8("hero4"))
        self.verticalLayout.addWidget(self.hero4)
        self.hero5 = QtGui.QComboBox(self.centralwidget)
        self.hero5.setObjectName(_fromUtf8("hero5"))
        self.verticalLayout.addWidget(self.hero5)
        self.calculate_button = QtGui.QPushButton(self.centralwidget)
        self.calculate_button.setObjectName(_fromUtf8("calculate_button"))
        self.verticalLayout.addWidget(self.calculate_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        HeroSelect.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(HeroSelect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 272, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        HeroSelect.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(HeroSelect)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HeroSelect.setStatusBar(self.statusbar)
        self.actionDump_Data = QtGui.QAction(HeroSelect)
        self.actionDump_Data.setObjectName(_fromUtf8("actionDump_Data"))
        self.menuFile.addAction(self.actionDump_Data)
        self.menubar.addAction(self.menuFile.menuAction())
        for i in range(0, self.list_length + 1):
            self.hero1.addItem(_fromUtf8(""))
            self.hero2.addItem(_fromUtf8(""))
            self.hero3.addItem(_fromUtf8(""))
            self.hero4.addItem(_fromUtf8(""))
            self.hero5.addItem(_fromUtf8(""))

        self.retranslateUi(HeroSelect)
        QtCore.QMetaObject.connectSlotsByName(HeroSelect)

    def retranslateUi(self, HeroSelect):
        HeroSelect.setWindowTitle(_translate("HeroSelect", "HeroSelect", None))
        self.label.setText(_translate("HeroSelect", "Select the Enemy Heroes", None))
        self.hero1.setItemText(0, _translate("HeroSelect", "", None))
        self.hero2.setItemText(0, _translate("HeroSelect", "", None))
        self.hero3.setItemText(0, _translate("HeroSelect", "", None))
        self.hero4.setItemText(0, _translate("HeroSelect", "", None))
        self.hero5.setItemText(0, _translate("HeroSelect", "", None))
        # populates the drop down boxes with all the heroes listed
        for i in range(1, self.list_length + 1):
            self.hero1.setItemText(i, _translate("HeroSelect", self.hero_list[i-1], None))
            self.hero2.setItemText(i, _translate("HeroSelect", self.hero_list[i-1], None))
            self.hero3.setItemText(i, _translate("HeroSelect", self.hero_list[i-1], None))
            self.hero4.setItemText(i, _translate("HeroSelect", self.hero_list[i-1], None))
            self.hero5.setItemText(i, _translate("HeroSelect", self.hero_list[i-1], None))
        self.calculate_button.setText(_translate("HeroSelect", "Calculate", None))
        self.calculate_button.clicked.connect(self.calculate)
        self.menuFile.setTitle(_translate("HeroSelect", "File", None))
        self.actionDump_Data.setText(_translate("HeroSelect", "Update Data", None))
        self.actionDump_Data.triggered.connect(self.fetch_data)

    # gets the matchup data from dotabuff
    def fetch_data(self):
        self.dumper.write_table()
        self.rows = self.analysis.read_table()

    # takes input from the GUI, tests all heroes against the given heroes, and outputs the sum of all the matchup data
    def calculate(self):
        hero_count = 0
        hero_list = []
        found = set()
        enemy_hero = []
        hero_list.append(self.hero1.currentIndex())
        hero_list.append(self.hero2.currentIndex())
        hero_list.append(self.hero3.currentIndex())
        hero_list.append(self.hero4.currentIndex())
        hero_list.append(self.hero5.currentIndex())
        # removes duplicates and blank hero selection.
        for i in hero_list:
            if i == 0:
                hero_list.pop(i)
                continue
            if i not in found:
                found.add(i)
                enemy_hero.append(i)
        # populates the list of values. These values will be the sum of the matchup values of all heroes
        for i in range(0, self.analysis.list_length):
                self.values[self.analysis.clean_list[i]] = 0
        # adjusts the values by checking input heroes one by one
        for hero_index in enemy_hero:
            self.values = self.analysis.analyze(self.values, self.rows, self.clean_list[hero_index-1])
            hero_count+=1
        if hero_count != 0:
            for i in range(0, self.analysis.list_length):
                self.values[self.analysis.clean_list[i]] = round(self.values[self.analysis.clean_list[i]] -
                                                                 (self.analysis.average * hero_count), 2)
        # removes input heroes from output list.
        for hero_index in enemy_hero:
            self.values.pop(self.clean_list[hero_index-1])
        # rounds all final data for output
        ret = self.analysis.sort(self.values)
        print "---------------------"
        for i in range(0, len(self.values)):
            print ret[i]



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HeroSelect = QtGui.QMainWindow()
    ui = Ui_HeroSelect()
    ui.setupUi(HeroSelect)
    HeroSelect.show()
    sys.exit(app.exec_())

