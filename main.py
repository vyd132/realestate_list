import PySide6,ui_mainwindow,locale,datetime,add_widget
from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter
from PySide6.QtCore import QStringListModel,QModelIndex,QTime,QDate,QLocale
from PySide6.QtGui import QStandardItemModel,QStandardItem

def add_data(data):
    model.appendRow([])
    model.setData(model.index(model.rowCount()-1, 0),data)

def get_data():
    data=lambda col:model.data(model.index(ui.tableView.currentIndex().row(),col))
    name=data(0)



app=QApplication()
main_window=QMainWindow()

add_window= add_widget.AddWidget(add_data)

ui=ui_mainwindow.Ui_MainWindow()
ui.setupUi(main_window)

model=QStandardItemModel(0,2)
model.setHorizontalHeaderLabels(['Название'])
ui.tableView.setModel(model)

ui.tableView.doubleClicked.connect(add_window.show)




ui.add_button.clicked.connect(add_window.new_ad_window_open)


main_window.show()
app.exec()