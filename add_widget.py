import PySide6,ui_mainwindow,locale,datetime,ui_realestate_form
from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget
from PySide6.QtCore import QStringListModel,QModelIndex,QTime,QDate,QLocale
from PySide6.QtGui import QStandardItemModel,QStandardItem

class AddWidget(QWidget,ui_realestate_form.Ui_Form):
    def __init__(self,on_ok):
        QWidget.__init__(self)
        ui_realestate_form.Ui_Form.__init__(self)
        self.setupUi(self)
        self.on_ok=on_ok
        self.okbutton.clicked.connect(self.new_row_add)

    def new_ad_window_open(self):
        self.show()




    def new_row_add(self):
        self.on_ok(self.name_edit.text())
        self.name_edit.setText('')
        self.close()