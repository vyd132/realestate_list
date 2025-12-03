import PySide6,ui_mainwindow,locale,datetime
from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter
from PySide6.QtCore import QStringListModel,QModelIndex,QTime,QDate,QLocale
from PySide6.QtGui import QStandardItemModel,QStandardItem

app=QApplication()
main_window=QMainWindow()

ui=ui_mainwindow.Ui_MainWindow()
ui.setupUi(main_window)

main_window.show()
app.exec()