import sys, csv, iconssearch1

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# loading data from csv
file = open("books.csv", mode="r", encoding="utf-8")
book_list = list(csv.DictReader(file))


class Ui_SearchForm(object):

    # the logics of our function
    ##################################################################################################################

    # return to admin page
    def adminpage(self):
        from main import Ui_AdminForm
        self.window1 = QtWidgets.QWidget()
        self.ui = Ui_AdminForm()
        self.ui.setupUi(self.window1)
        self.window1.show()

        # searching book
        #################################################################################

    def display(self):
        # getting the values of category and search word
        search_by = self.search_by_combobox.currentText()
        keyword = self.search_text.text()

        # when nothing is entered in both search by
        if len(search_by) == 0 or search_by == "< Select Category >":
            msg = QMessageBox()
            msg.setWindowTitle("Search Error")
            msg.setText("Select Category to search by")
            x = msg.exec_()
            return

        # when nothing is entered in search keyword
        if len(keyword) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Search Error")
            msg.setText("Enter keyword to search")
            x = msg.exec_()
            return

        # variable for storing the matches of the search
        result_books = []

        # search book by Title
        if search_by == "Title":
            for book in book_list:
                if keyword.lower() in book[search_by].lower():
                    result_books.append(dict(book))

        # search book by Author
        elif search_by == "Author":
            for book in book_list:
                if keyword.lower() in book[search_by].lower():
                    result_books.append(book)

        # search book by Genre
        elif search_by == "Genre":
            for book in book_list:
                if keyword.lower() == book[search_by].lower():
                    new_dict = {'Title': book["Title"], 'Author': book["Author"], 'Genre': book["Genre"]}
                    result_books.append(new_dict)

        # if no results found
        if len(result_books) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Search Results")
            msg.setText("Check spellings or book does not exits")
            x = msg.exec_()
            return

        else:
            # Populate table by search
            #################################################
            row = 0
            self.Booktable.setRowCount(len(result_books))
            for person in result_books:
                self.Booktable.setItem(row, 0, QtWidgets.QTableWidgetItem(person["Title"]))
                self.Booktable.setItem(row, 1, QtWidgets.QTableWidgetItem(person["Author"]))
                self.Booktable.setItem(row, 2, QtWidgets.QTableWidgetItem(person["Genre"]))
                row += 1
            msg = QMessageBox()
            msg.setWindowTitle("Search Results")
            msg.setText(f"Found {len(result_books)} match(es)")
            x = msg.exec_()
            #################################################################################

    # Filling the table with all the data from csv
    #################################################################################
    def load_data(self):
        row = 0
        self.Booktable.setRowCount(len(book_list))
        for person in book_list:
            self.Booktable.setItem(row, 0, QtWidgets.QTableWidgetItem(person["Title"]))
            self.Booktable.setItem(row, 1, QtWidgets.QTableWidgetItem(person["Author"]))
            self.Booktable.setItem(row, 2, QtWidgets.QTableWidgetItem(person["Genre"]))
            row += 1

    # the logics of Gui app
    ##################################################################################################################

    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(625, 565)

        # removes the close button and makes background translucent
        ###########################################################################################
        SearchForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        SearchForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.widget = QtWidgets.QWidget(SearchForm)
        self.widget.setGeometry(QtCore.QRect(40, 40, 561, 511))
        self.widget.setStyleSheet("QPushButton#search_book_button{\n"
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
                                  "\n"
                                  "QPushButton#reload_button{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255));\n "
                                  "    color:rgba(255,255,255,210);\n"
                                  "    border-radius:5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#reload_button:hover{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
                                  "stop:0 rgba(255, 123, 29, 255), stop:1 rgba(40, 22, 22, 255));\n "
                                  "}\n"
                                  "\n"
                                  "QPushButton#reload_button:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    background-color:rgba(255, 123, 29, 255);\n"
                                  "}")
        self.widget.setObjectName("widget")

        # Labels
        #################################################################################
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 9, 541, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/iconsadd/icons/pexels-olena-bohovyk-3646172.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.table = QtWidgets.QLabel(self.widget)
        self.table.setGeometry(QtCore.QRect(9, 179, 541, 291))
        self.table.setText("")
        self.table.setObjectName("table")

        self.Add_Book_side = QtWidgets.QLabel(self.widget)
        self.Add_Book_side.setGeometry(QtCore.QRect(20, 20, 511, 151))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Add_Book_side.setFont(font)
        self.Add_Book_side.setStyleSheet("background-color:rgba(100,100,100,80);\n"
                                         "border-top-right-radius:50px;\n"
                                         "border-bottom-right-radius:50px;\n"
                                         "border-top-left-radius:50px;\n"
                                         "border-bottom-left-radius:50px;")
        self.Add_Book_side.setText("")
        self.Add_Book_side.setObjectName("Add_Book_side")

        self.Add_Book_label = QtWidgets.QLabel(self.widget)
        self.Add_Book_label.setGeometry(QtCore.QRect(210, 10, 171, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Add_Book_label.setFont(font)
        self.Add_Book_label.setObjectName("Add_Book_label")

        # Search by ComboBox
        #################################################################################
        self.search_by_combobox = QtWidgets.QComboBox(self.widget)
        self.search_by_combobox.setGeometry(QtCore.QRect(180, 60, 211, 22))
        self.search_by_combobox.setEditable(False)
        self.search_by_combobox.setPlaceholderText("")
        self.search_by_combobox.setObjectName("search_by_combobox")
        self.search_by_combobox.addItem("")
        self.search_by_combobox.addItem("")
        self.search_by_combobox.addItem("")
        self.search_by_combobox.addItem("")

        # Search text
        #################################################################################
        self.search_text = QtWidgets.QLineEdit(self.widget)
        self.search_text.setGeometry(QtCore.QRect(180, 99, 211, 21))
        self.search_text.setObjectName("search_text")

        # Search button
        #################################################################################
        self.search_book_button = QtWidgets.QPushButton(self.widget)
        self.search_book_button.setGeometry(QtCore.QRect(230, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.search_book_button.setFont(font)
        self.search_book_button.setObjectName("search_book_button")

        # Book Table
        #################################################################################
        self.Booktable = QtWidgets.QTableWidget(self.widget)
        self.Booktable.setGeometry(QtCore.QRect(30, 200, 501, 281))
        self.Booktable.setStyleSheet("")
        self.Booktable.setObjectName("Booktable")
        self.Booktable.setColumnCount(3)
        self.Booktable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Booktable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Booktable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Booktable.setHorizontalHeaderItem(2, item)

        # Close button
        #################################################################################
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setGeometry(QtCore.QRect(520, 10, 31, 31))
        self.close_button.setStyleSheet("background-color:rgba(0,0,0,0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconsadd/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setObjectName("close_button")
        # Close window
        self.close_button.clicked.connect(lambda: SearchForm.close())

        # Home button
        #################################################################################
        self.home_button = QtWidgets.QPushButton(self.widget)
        self.home_button.setGeometry(QtCore.QRect(10, 10, 31, 23))
        self.home_button.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.home_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconsadd/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setObjectName("home_button")

        # Reload button
        #################################################################################
        self.reload_button = QtWidgets.QPushButton(self.widget)
        self.reload_button.setGeometry(QtCore.QRect(470, 180, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.reload_button.setFont(font)
        self.reload_button.setObjectName("reload_button")

        self.retranslateUi(SearchForm)
        self.search_by_combobox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)

        # Size of columns
        ##################################################################

        self.Booktable.setColumnWidth(0, 160)
        self.Booktable.setColumnWidth(1, 170)
        self.Booktable.setColumnWidth(2, 170)

        # Load data from books.csv
        ##################################################################
        self.load_data()

        # refresh button
        self.reload_button.pressed.connect(self.load_data)
        # search button clicked
        self.search_book_button.pressed.connect(self.display)

        # Home button is clicked
        self.home_button.clicked.connect(self.adminpage)
        self.home_button.clicked.connect(SearchForm.close)

    def retranslateUi(self, SearchForm):
        _translate = QtCore.QCoreApplication.translate
        SearchForm.setWindowTitle(_translate("SearchForm", "Form"))
        self.Add_Book_label.setText(_translate("SearchForm", "Search Book"))
        self.search_by_combobox.setCurrentText(_translate("SearchForm", "< Select Category >"))
        self.search_by_combobox.setItemText(0, _translate("SearchForm", "< Select Category >"))
        self.search_by_combobox.setItemText(1, _translate("SearchForm", "Title"))
        self.search_by_combobox.setItemText(2, _translate("SearchForm", "Author"))
        self.search_by_combobox.setItemText(3, _translate("SearchForm", "Genre"))
        self.search_text.setPlaceholderText(_translate("SearchForm", "Title/Author/Genre"))
        self.search_book_button.setText(_translate("SearchForm", "Search"))
        item = self.Booktable.horizontalHeaderItem(0)
        item.setText(_translate("SearchForm", "Title"))
        item = self.Booktable.horizontalHeaderItem(1)
        item.setText(_translate("SearchForm", "Author"))
        item = self.Booktable.horizontalHeaderItem(2)
        item.setText(_translate("SearchForm", "Genre"))
        self.reload_button.setText(_translate("SearchForm", "Refresh"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QWidget()
    ui = Ui_SearchForm()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
