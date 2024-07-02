import sys
import iconsmain

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminForm(object):

    # the logics of our function

    ##################################################################################################################

    # go to search page
    def searchpage(self):
        from searchbook import Ui_SearchForm
        self.window1 = QtWidgets.QWidget()
        self.ui = Ui_SearchForm()
        self.ui.setupUi(self.window1)
        self.window1.show()

    # go to add page
    def addpage(self):
        from addBook import Ui_AddBook
        self.window1 = QtWidgets.QWidget()
        self.ui = Ui_AddBook()
        self.ui.setupUi(self.window1)
        self.window1.show()

        # the logics of Gui app

    #################################################################################################################

    def setupUi(self, AdminForm):
        AdminForm.setObjectName("AdminForm")
        AdminForm.resize(625, 565)

        # removes the close button and makes backgrpund translucent
        ###########################################################################################
        AdminForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AdminForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.widget = QtWidgets.QWidget(AdminForm)
        self.widget.setGeometry(QtCore.QRect(30, 30, 561, 500))
        self.widget.setStyleSheet("QPushButton#add_book_button{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255));\n "
                                  "    color:rgba(255,255,255,210);\n"
                                  "    border-radius:5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#add_book_button:hover{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255), "
                                  "stop:1 rgba(40, 22, 22, 255));\n "
                                  "}\n"
                                  "\n"
                                  "QPushButton#add_book_button:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    background-color:rgba(255, 123, 29, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#search_book_button{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255));\n "
                                  "    color:rgba(255,255,255,210);\n"
                                  "    border-radius:5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#search_book_button:hover{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255), stop:1 rgba(40, 22, 22, 255));\n "
                                  "}\n"
                                  "\n"
                                  "QPushButton#search_book_button:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    background-color:rgba(255, 123, 29, 255);\n"
                                  "}\n"
                                  "")
        self.widget.setObjectName("widget")
        self.imageside = QtWidgets.QLabel(self.widget)
        self.imageside.setGeometry(QtCore.QRect(0, 30, 280, 430))
        self.imageside.setText("")
        self.imageside.setPixmap(QtGui.QPixmap(":/icons/icons/pexels-wilson-vitorino-2167677.jpg"))
        self.imageside.setScaledContents(True)
        self.imageside.setObjectName("imageside")
        self.login_side = QtWidgets.QLabel(self.widget)
        self.login_side.setGeometry(QtCore.QRect(270, 30, 291, 430))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.login_side.setFont(font)
        self.login_side.setStyleSheet("background-color:rgba(255,255,255,255);\n"
                                      "border-top-right-radius:50px;\n"
                                      "border-bottom-right-radius:50px;")
        self.login_side.setText("")
        self.login_side.setObjectName("login_side")
        self.login_label = QtWidgets.QLabel(self.widget)
        self.login_label.setGeometry(QtCore.QRect(370, 70, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.notes = QtWidgets.QLabel(self.widget)
        self.notes.setGeometry(QtCore.QRect(330, 140, 201, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.notes.setFont(font)
        self.notes.setObjectName("notes")

        # Search Button
        ##################################################################
        self.search_book_button = QtWidgets.QPushButton(self.widget)
        self.search_book_button.setGeometry(QtCore.QRect(320, 220, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.search_book_button.setFont(font)
        self.search_book_button.setObjectName("search_book_button")

        # Add  Button
        ##################################################################
        self.add_book_button = QtWidgets.QPushButton(self.widget)
        self.add_book_button.setGeometry(QtCore.QRect(320, 320, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_book_button.setFont(font)
        self.add_book_button.setObjectName("add_book_button")

        # Close button
        ##################################################################
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setGeometry(QtCore.QRect(520, 40, 31, 31))
        self.close_button.setStyleSheet("background-color:rgba(0,0,0,0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setObjectName("close_button")

        # Close window
        self.close_button.clicked.connect(lambda: AdminForm.close())

        self.retranslateUi(AdminForm)
        QtCore.QMetaObject.connectSlotsByName(AdminForm)

        # When buttons are clicked
        ####################################################################################
        # Search button clicked
        self.search_book_button.clicked.connect(self.searchpage)
        self.search_book_button.clicked.connect(AdminForm.close)
        # Add book button clicked
        self.add_book_button.clicked.connect(self.addpage)
        self.add_book_button.clicked.connect(AdminForm.close)

    def retranslateUi(self, AdminForm):
        _translate = QtCore.QCoreApplication.translate
        AdminForm.setWindowTitle(_translate("AdminForm", "Form"))
        self.login_label.setText(_translate("AdminForm", "Library"))
        self.notes.setText(_translate("AdminForm", "Welcome user, click your option"))
        self.search_book_button.setText(_translate("AdminForm", "Search Book"))
        self.add_book_button.setText(_translate("AdminForm", "Add Book"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AdminForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

