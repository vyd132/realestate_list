import PySide6,ui_mainwindow,locale,datetime,add_widget
from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter
from PySide6.QtCore import QStringListModel,QModelIndex,QTime,QDate,QLocale
from PySide6.QtGui import QStandardItemModel,QStandardItem

def add_data(name,id):
    global id_num
    if id!=None:
        model.setData(model.index(id, 0), name)
        return
    model.appendRow([])
    ui.tableView.setCurrentIndex(model.index(model.rowCount()-1, 0))
    model.setData(model.index(model.rowCount()-1, 2), id_num)
    id_num+=1
    model.setData(model.index(model.rowCount()-1, 0), name)

def get_data():
    data=lambda col:model.data(model.index(ui.tableView.currentIndex().row(),col))
    name=data(0)
    id=data(2)
    add_window.row_edit(name,id)


id_num=0

app=QApplication()
main_window=QMainWindow()

add_window= add_widget.AddWidget(add_data)

ui=ui_mainwindow.Ui_MainWindow()
ui.setupUi(main_window)

model=QStandardItemModel(0,3)
model.setHorizontalHeaderLabels(['Название','Адрес','ID'])

ui.tableView.setModel(model)

# ui.tableView.hideColumn(2)

ui.tableView.doubleClicked.connect(get_data)




ui.add_button.clicked.connect(add_window.new_ad_window_open)


main_window.show()
app.exec()