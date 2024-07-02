import sys, csv
import iconsadd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Ui_AddBook(object):

    # the logics of our function
    ##################################################################################################################

    # return to admin page function
    def adminpage(self):
        from main import Ui_AdminForm
        self.window1 = QtWidgets.QWidget()
        self.ui = Ui_AdminForm()
        self.ui.setupUi(self.window1)
        self.window1.show()

    # Add new book function

    def add_new_book(self):
        # Getting values from text fields
        title = self.book_title_text.text()
        author = self.book_author_text.text()
        genre = self.comboBox.currentText()

        # when title is null
        if len(title) == 0:
            msg = QMessageBox()
            msg.setWindowTitle('Adding Error')
            msg.setText("The title field cannot be empty")
            x = msg.exec_()
            return

        # adding new book
        new_book = Book(title, author, genre)
        with open("books.csv", mode="a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Genre"])
            writer.writerow({"Title": new_book.title,
                             "Author": new_book.author, "Genre": new_book.genre})
        # success message
        msg = QMessageBox()
        msg.setWindowTitle('Adding new book')
        msg.setText(f"{title} added successfully")
        x = msg.exec_()

        # clearing the fields after adding
        self.book_author_text.clear()
        self.book_title_text.clear()

    # the logics of Gui app
    ##################################################################################################################

    def setupUi(self, AddBook):
        AddBook.setObjectName("AddBook")
        AddBook.resize(625, 565)
        self.widget = QtWidgets.QWidget(AddBook)
        self.widget.setGeometry(QtCore.QRect(30, 30, 561, 500))

        # removes the close button and makes backgrpund translucent
        ###########################################################################################
        AddBook.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AddBook.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.widget.setStyleSheet("QPushButton#add_book_button{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255));\n "
                                  "    color:rgba(255,255,255,210);\n"
                                  "    border-radius:5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#add_book_button:hover{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255), stop:1 rgba(40, 22, 22, 255));\n "
                                  "}\n"
                                  "\n"
                                  "QPushButton#add_book_button:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    background-color:rgba(255, 123, 29, 255);\n"
                                  "}\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 30, 280, 430))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/iconsadd/icons/pexels-lisa-fotios-2090104.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.Add_Book_side = QtWidgets.QLabel(self.widget)
        self.Add_Book_side.setGeometry(QtCore.QRect(270, 30, 291, 430))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Add_Book_side.setFont(font)
        self.Add_Book_side.setStyleSheet("background-color:rgba(255,255,255,255);\n"
                                         "border-top-right-radius:50px;\n"
                                         "border-bottom-right-radius:50px;")
        self.Add_Book_side.setText("")
        self.Add_Book_side.setObjectName("Add_Book_side")
        self.Add_Book_label = QtWidgets.QLabel(self.widget)
        self.Add_Book_label.setGeometry(QtCore.QRect(360, 70, 141, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Add_Book_label.setFont(font)
        self.Add_Book_label.setObjectName("Add_Book_label")

        self.book_title_text = QtWidgets.QLineEdit(self.widget)
        self.book_title_text.setGeometry(QtCore.QRect(320, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_title_text.setFont(font)
        self.book_title_text.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                           "border:none;\n"
                                           "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                           "color:rgba(0,0,0, 240);\n"
                                           "padding-bottom:7px;")
        self.book_title_text.setObjectName("book_title_text")
        self.book_author_text = QtWidgets.QLineEdit(self.widget)
        self.book_author_text.setGeometry(QtCore.QRect(320, 220, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_author_text.setFont(font)
        self.book_author_text.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                            "color:rgba(0,0,0, 240);\n"
                                            "padding-bottom:7px;")
        self.book_author_text.setObjectName("book_author_text")

        # Add book button
        #################################################################################
        self.add_book_button = QtWidgets.QPushButton(self.widget)
        self.add_book_button.setGeometry(QtCore.QRect(320, 370, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_book_button.setFont(font)
        self.add_book_button.setObjectName("add_book_button")

        # Close button
        #################################################################################
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setGeometry(QtCore.QRect(520, 40, 31, 31))
        self.close_button.setStyleSheet("background-color:rgba(0,0,0,0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconsadd/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setObjectName("close_button")
        # Close window
        self.close_button.clicked.connect(lambda: AddBook.close())

        # Home button
        #################################################################################
        self.home_button = QtWidgets.QPushButton(self.widget)
        self.home_button.setGeometry(QtCore.QRect(270, 40, 31, 23))
        self.home_button.setStyleSheet("background-color: rgb(0, 0, 0,0);")
        self.home_button.setText("")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconsadd/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setObjectName("home_button")

        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(320, 310, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(320, 280, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AddBook)
        QtCore.QMetaObject.connectSlotsByName(AddBook)

        # when buttons are clicked
        ##########################################
        # add button clicked
        self.add_book_button.pressed.connect(self.add_new_book)
        # home button clicked
        self.home_button.pressed.connect(self.adminpage)
        self.home_button.pressed.connect(AddBook.close)

    ###########################################################################################################

    def retranslateUi(self, AddBook):
        _translate = QtCore.QCoreApplication.translate
        AddBook.setWindowTitle(_translate("AddBook", "Form"))
        self.Add_Book_label.setText(_translate("AddBook", "New Book"))
        self.book_title_text.setPlaceholderText(_translate("AddBook", "Title"))
        self.book_author_text.setPlaceholderText(_translate("AddBook", "Author"))
        self.add_book_button.setText(_translate("AddBook", "Add Book"))
        self.comboBox.setItemText(0, _translate("AddBook", "Fiction"))
        self.comboBox.setItemText(1, _translate("AddBook", "Non-fiction"))
        self.comboBox.setItemText(2, _translate("AddBook", "History"))
        self.comboBox.setItemText(3, _translate("AddBook", "Philosophy"))
        self.comboBox.setItemText(4, _translate("AddBook", "Science"))
        self.comboBox.setItemText(5, _translate("AddBook", "Mathematics"))
        self.comboBox.setItemText(6, _translate("AddBook", "Data Science"))
        self.comboBox.setItemText(7, _translate("AddBook", "Computer Science"))
        self.comboBox.setItemText(8, _translate("AddBook", "Comics"))
        self.comboBox.setItemText(9, _translate("AddBook", "Signal Processing"))
        self.label_2.setText(_translate("AddBook", "Genre"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QWidget()
    ui = Ui_AddBook()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())
