from PyQt5 import QtCore, QtGui, QtWidgets
from core import Manager
from utils import Alerts
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(699, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 625))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 161, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(1)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 119, 620, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("border-color: rgb(85, 85, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.todos_tab = QtWidgets.QWidget()
        self.todos_tab.setObjectName("todos_tab")
        self.listView = QtWidgets.QListWidget(self.todos_tab)
        self.listView.setGeometry(QtCore.QRect(20, 70, 431, 221))
        self.listView.setObjectName("listView")
        self.add_todo_input = QtWidgets.QLineEdit(self.todos_tab)
        self.add_todo_input.setGeometry(QtCore.QRect(20, 30, 430, 31))
        self.add_todo_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.add_todo_input.setObjectName("add_todo_input")
        self.add_todo_btn = QtWidgets.QPushButton(self.todos_tab, clicked=lambda: self.add_todo())
        self.add_todo_btn.setGeometry(QtCore.QRect(470, 30, 110, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image_add/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_todo_btn.setIcon(icon)
        self.add_todo_btn.setIconSize(QtCore.QSize(25, 25))
        self.add_todo_btn.setObjectName("add_todo_btn")
        self.delete_todo = QtWidgets.QPushButton(self.todos_tab, clicked=lambda: self.remove_todo())
        self.delete_todo.setGeometry(QtCore.QRect(20, 310, 180, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image_remove/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_todo.setIcon(icon1)
        self.delete_todo.setObjectName("delete_todo")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image_point/point_ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.todos_tab, icon2, "")
        self.tasks_done_tab = QtWidgets.QWidget()
        self.tasks_done_tab.setObjectName("tasks_done_tab")
        self.listView_2 = QtWidgets.QListWidget(self.tasks_done_tab)
        self.listView_2.setGeometry(QtCore.QRect(20, 50, 571, 270))
        self.listView_2.setObjectName("listView_2")
        self.label_2 = QtWidgets.QLabel(self.tasks_done_tab)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image_yes/yes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tasks_done_tab, icon3, "")
        self.r = QtWidgets.QLabel(self.centralwidget)
        self.r.setGeometry(QtCore.QRect(410, 530, 249, 30))
        self.r.setFrameShape(QtWidgets.QFrame.Box)
        self.r.setAlignment(QtCore.Qt.AlignCenter)
        self.r.setObjectName("r")
        self.slapper_image = QtWidgets.QLabel(self.centralwidget)
        self.slapper_image.setGeometry(QtCore.QRect(200, 20, 90, 80))
        self.slapper_image.setText("")
        self.slapper_image.setPixmap(QtGui.QPixmap(":/image_slap/slap_pixmap.jpg"))
        self.slapper_image.setScaledContents(True)
        self.slapper_image.setObjectName("slapper_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.listView_2.addItems(["You son of a bitch! You haven't done jack till now. You're a fcking lazy piece of shit.", "What are you even doing in this tab?", "Like, seriously? You think I'll list your accomplishments here? You are shit, nothing else. ", "You probably did one thing and now you're pretending to be a productive person? YOU AIN'T SHIT", "Be more, Get shit done!"])

        self.manager = Manager()
        self.list_todos()
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Todo Slap"))
        self.label.setText(_translate("MainWindow", "Todos Slapper!"))
        self.add_todo_input.setPlaceholderText(_translate("MainWindow", "Add Your To Do Text Here . . . "))
        self.add_todo_btn.setText(_translate("MainWindow", "Add Todo"))
        self.delete_todo.setText(_translate("MainWindow", "Remove Selected Todo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.todos_tab), _translate("MainWindow", "Your To Dos"))
        self.label_2.setText(_translate("MainWindow", "Completed Tasks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tasks_done_tab), _translate("MainWindow", "Tasks Done!"))
        self.r.setText(_translate("MainWindow", "All Rights Reserved @ A. Mujeeb Ishaque"))

    def list_todos(self):
        _todos = self.manager
        
        for item in _todos.connection.all():
            self.listView.addItem(item.get('todos'))
            
    def add_todo(self):
        _text = self.add_todo_input.text()
        if not _text or len(_text) < 5:
            Alerts.show_alert('error', 'ERROR: Empty todo? You want to do nothing? Add a valid todo, you dumb shit.')
            return
        self.listView.addItem(_text)
        self.manager.add_record(_text)
        self.add_todo_input.setText("")
    
    def remove_todo(self):
        item_clicked = self.listView.currentRow()
        item_clicked_text = self.listView.currentItem().text()
        self.manager.delete_record(item_clicked_text)
        self.listView.takeItem(item_clicked)

import add_rc
import minus_rc
import point_ico_rc
import slap_pixmap_rc
import yes_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
