import PySide6,ui_mainwindow,locale,datetime,add_widget
from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter
from PySide6.QtCore import QStringListModel,QModelIndex,QTime,QDate,QLocale,Qt
from PySide6.QtGui import QStandardItemModel,QStandardItem

def add_data(name,id,address,cost,check,description):
    global id_num
    row = id_check(id)
    if id is None:
        model.appendRow([])
        row=model.rowCount() - 1
        model.setData(model.index(row, 2), id_num)
        id_num += 1


    ui.tableView.setCurrentIndex(model.index(row, 0))


    model.setData(model.index(row, 0), name)
    model.setData(model.index(row, 1),address)
    model.setData(model.index(row, 3),cost)
    model.setData(model.index(row, 4), Qt.CheckState.Checked if check else Qt.CheckState.Unchecked,role=Qt.ItemDataRole.CheckStateRole)
    model.setData(model.index(row, 5), description)

def get_data():
    data=lambda col:model.data(model.index(ui.tableView.currentIndex().row(),col))
    name=data(0)
    address=data(1)
    id=data(2)
    cost=data(3)
    check=model.data(model.index(ui.tableView.currentIndex().row(),4),role=Qt.ItemDataRole.CheckStateRole)
    description=data(5)
    add_window.row_edit(name,id,address,cost,check==Qt.CheckState.Checked,description)

def id_check(id):
    for row_num in range(model.rowCount()):
        if model.data(model.index(row_num,2))==id:
            return row_num

id_num=0

app=QApplication()
main_window=QMainWindow()

add_window= add_widget.AddWidget(add_data)

ui=ui_mainwindow.Ui_MainWindow()
ui.setupUi(main_window)

model=QStandardItemModel(0,6)
model.setHorizontalHeaderLabels(['Название','Адрес','ID','Стоимость','Актуальность','Описание'])

ui.tableView.setModel(model)

ui.tableView.hideColumn(2)
ui.tableView.hideColumn(6)

ui.tableView.doubleClicked.connect(get_data)




ui.add_button.clicked.connect(add_window.new_ad_window_open)
ui.add_button.clicked.connect(lambda: print(model.data(model.index(0,0))))


main_window.show()
app.exec()