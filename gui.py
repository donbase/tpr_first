from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from solver import Solver
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
import pandas as pd
import csv


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 591, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 380, 591, 291))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 350, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_row)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete_row)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.add_column)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.delete_column)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.print_data_on_table2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 130, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.open_file_dialog)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 640, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.save_to_csv)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        combo_box = QtWidgets.QComboBox()
        combo_box.addItems(["min", "max"])
        self.tableWidget.setCellWidget(0, 0, combo_box)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "max/min"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Вес"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Точка 1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Функция 1"))
        self.label.setText(_translate("MainWindow", "Начальное множество"))
        self.label_2.setText(_translate("MainWindow", "Множество Парето + линейная свертка"))
        self.pushButton.setText(_translate("MainWindow", "+ "))
        self.label_3.setText(_translate("MainWindow", "Кол-во точек:"))
        self.label_4.setText(_translate("MainWindow", "Кол-во функций:"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "-"))
        self.pushButton_5.setText(_translate("MainWindow", "Вычислить"))
        self.pushButton_6.setText(_translate("MainWindow", "Загрузить данные из файла"))
        self.pushButton_7.setText(_translate("MainWindow", "Сохранить в файл"))

    def add_row(self):
        rows_cnt = self.tableWidget.rowCount()
        if rows_cnt < 20 + 2:
            self.tableWidget.insertRow(rows_cnt)
            header_item = QtWidgets.QTableWidgetItem(f"Точка {rows_cnt - 1}")
            self.tableWidget.setVerticalHeaderItem(rows_cnt, header_item)

    def delete_row(self):
        rows_cnt = self.tableWidget.rowCount()
        if rows_cnt > 3:
            self.tableWidget.removeRow(rows_cnt - 1)

    def add_column(self):
        columns_cnt = self.tableWidget.columnCount()
        if columns_cnt < 10:
            self.tableWidget.insertColumn(columns_cnt)
            header_item = QtWidgets.QTableWidgetItem(f"Функция {columns_cnt + 1}")
            self.tableWidget.setHorizontalHeaderItem(columns_cnt, header_item)
            combo_box = QtWidgets.QComboBox()
            combo_box.addItems(["min", "max"])
            self.tableWidget.setCellWidget(0, columns_cnt, combo_box)

    def delete_column(self):
        columns_cnt = self.tableWidget.columnCount()
        if columns_cnt > 1:
            self.tableWidget.removeColumn(columns_cnt - 1)

    def read_data_from_table1(self):
        row_count = self.tableWidget.rowCount()
        column_count = self.tableWidget.columnCount()
        directions = []
        weights = []
        data = []
        for column in range(column_count):
            widget = self.tableWidget.cellWidget(0, column)
            directions.append(widget.currentText())

        for column in range(column_count):
            item = self.tableWidget.item(1, column)
            if item is not None:
                weights.append(int(item.text()))
            else:
                weights.append(0)

        for row in range(2, row_count):
            data.append([self.tableWidget.verticalHeaderItem(row).text()])
            for column in range(column_count):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    data[-1].append(int(item.text()))
                else:
                    data[-1].append(0)

        return directions, weights, data

    def print_data_on_table2(self):
        directions, weights, data = self.read_data_from_table1()
        solver = Solver(len(data[0]) - 1, len(data), data, weights, directions)
        pareto_set = solver.create_pareto()
        print(pareto_set)

        self.tableWidget_2.clear()  # Удаляет все элементы
        self.tableWidget_2.setRowCount(len(pareto_set))
        if pareto_set:
            self.tableWidget_2.setColumnCount(len(pareto_set[0]))
        else:
            self.tableWidget_2.setColumnCount(0)

        for row in range(self.tableWidget_2.rowCount()):
            header_item = QtWidgets.QTableWidgetItem(pareto_set[row][0])
            self.tableWidget_2.setVerticalHeaderItem(row, header_item)

        for col in range(self.tableWidget_2.columnCount() - 1):
            header = self.tableWidget.horizontalHeaderItem(col).text()
            header_item = QtWidgets.QTableWidgetItem(header)
            self.tableWidget_2.setHorizontalHeaderItem(col, header_item)
        header_item = QtWidgets.QTableWidgetItem('Свертка(итого)')
        self.tableWidget_2.setHorizontalHeaderItem(self.tableWidget_2.columnCount() - 1, header_item)

        for row in range(self.tableWidget_2.rowCount()):
            for col in range(self.tableWidget_2.columnCount() - 1):
                item = str(pareto_set[row][col + 1])
                item = QtWidgets.QTableWidgetItem(item)
                self.tableWidget_2.setItem(row, col, item)

        convolution = solver.convolution(pareto_set)
        for row in range(self.tableWidget_2.rowCount()):
            item = QtWidgets.QTableWidgetItem(str(convolution[row]))
            self.tableWidget_2.setItem(row, self.tableWidget_2.columnCount() - 1, item)


    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*)", options=options)
        try:
            # Чтение данных из CSV файла
            data = pd.read_csv(file_name)
            print(data)
            print(data.shape[0])
            print(data.shape[1])
            print(data.columns[1:])
            self.tableWidget.clear()
            # Установка размеров таблицы
            self.tableWidget.setRowCount(data.shape[0])
            self.tableWidget.setColumnCount(data.shape[1] - 1)
            self.tableWidget.setHorizontalHeaderLabels(data.columns[1:])
            updated_second_column = pd.Series(['min/max', 'Вес'] + data.iloc[2:, 0].tolist())
            self.tableWidget.setVerticalHeaderLabels(updated_second_column)

            columns_cnt = self.tableWidget.columnCount()
            for i in range(columns_cnt):
                combo_box = QtWidgets.QComboBox()
                combo_box.addItems(["min", "max"])
                self.tableWidget.setCellWidget(0, i, combo_box)

            for row in range(data.shape[0]):
                for column in range(1, data.shape[1]):
                    item = QtWidgets.QTableWidgetItem(str(data.iat[row, column]))
                    self.tableWidget.setItem(row, column - 1, item)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")

    def save_to_csv(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)
        if file_name:
            try:
                with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)

                    row_count = self.tableWidget_2.rowCount()
                    column_count = self.tableWidget_2.columnCount()

                    header_row = ['name']
                    for column in range(column_count):
                        header_item = self.tableWidget_2.horizontalHeaderItem(column)
                        header_row.append(header_item.text() if header_item else "")
                    writer.writerow(header_row)

                    # Записываем данные в CSV
                    for row in range(row_count):
                        row_data = [
                            self.tableWidget_2.verticalHeaderItem(row).text() if self.tableWidget_2.verticalHeaderItem(
                                row) else ""]
                        for column in range(column_count):
                            item = self.tableWidget_2.item(row, column)
                            row_data.append(item.text() if item else "")
                        writer.writerow(row_data)

                QMessageBox.information(self, "Успех", "Файл успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении файла: {e}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
