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
        self.cancel_button.clicked.connect(self.close)
        self.id=None

    def new_ad_window_open(self):
        self.name_edit.setText('')
        self.address_edit.setText('')
        self.value_box.setValue(0)
        self.actuality_box.setChecked(True)
        self.description_edit.setText('')
        self.show()



    def row_edit(self,name,id,address,cost,check,description):
        self.name_edit.setText(name)
        self.address_edit.setText(address)
        self.value_box.setValue(cost)
        self.actuality_box.setChecked(check)
        self.description_edit.setText(description)
        self.id=id
        self.show()


    def new_row_add(self):
        self.on_ok(self.name_edit.text(),self.id,self.address_edit.text(),self.value_box.value(),self.actuality_box.isChecked(),self.description_edit.toPlainText())
        self.id=None
        self.close()