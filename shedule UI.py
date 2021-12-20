import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="telebot",
                                     user="postgres",
                                     password="1234",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.monday_tab = QWidget()
        self.tuesday_tab = QWidget()
        self.wednesday_tab = QWidget()
        self.thursday_tab = QWidget()
        self.friday_tab = QWidget()
        self.teacher_tab = QWidget()
        self.subject_tab = QWidget()

        self.tabs.addTab(self.monday_tab, "Понедельник")
        self.tabs.addTab(self.tuesday_tab, "Вторник")
        self.tabs.addTab(self.wednesday_tab, "Среда")
        self.tabs.addTab(self.thursday_tab, "Четверг")
        self.tabs.addTab(self.friday_tab, "Пятница")
        self.tabs.addTab(self.teacher_tab, "Преподаватели")
        self.tabs.addTab(self.subject_tab, "Предметы")

        self.monday_gbox = QGroupBox("Понедельник")
        self.tuesday_gbox = QGroupBox("Вторник")
        self.wednesday_gbox = QGroupBox("Среда")
        self.thursday_gbox = QGroupBox("Четверг")
        self.friday_gbox = QGroupBox("Пятница")
        self.teacher_gbox = QGroupBox("Преподаватели")
        self.subject_gbox = QGroupBox("Предметы")

        self.svbox1 = QVBoxLayout()
        self.svbox2 = QVBoxLayout()
        self.svbox3 = QVBoxLayout()
        self.svbox4 = QVBoxLayout()
        self.svbox5 = QVBoxLayout()
        self.svbox6 = QVBoxLayout()
        self.svbox7 = QVBoxLayout()
        self.svbox = QVBoxLayout()

        self.shbox_monday = QHBoxLayout()
        self.shbox_tuesday = QHBoxLayout()
        self.shbox_wednesday = QHBoxLayout()
        self.shbox_thursday = QHBoxLayout()
        self.shbox_friday = QHBoxLayout()
        self.shbox_teacher = QHBoxLayout()
        self.shbox_subject = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox1.addLayout(self.shbox_monday)
        self.svbox2.addLayout(self.shbox_tuesday)
        self.svbox3.addLayout(self.shbox_wednesday)
        self.svbox4.addLayout(self.shbox_thursday)
        self.svbox5.addLayout(self.shbox_friday)
        self.svbox6.addLayout(self.shbox_teacher)
        self.svbox7.addLayout(self.shbox_subject)
        self.svbox.addLayout(self.shbox2)

        self.shbox_monday.addWidget(self.monday_gbox)
        self.shbox_tuesday.addWidget(self.tuesday_gbox)
        self.shbox_wednesday.addWidget(self.wednesday_gbox)
        self.shbox_thursday.addWidget(self.thursday_gbox)
        self.shbox_friday.addWidget(self.friday_gbox)
        self.shbox_teacher.addWidget(self.teacher_gbox)
        self.shbox_subject.addWidget(self.subject_gbox)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()
        self._create_thursday_table()
        self._create_friday_table()
        self._create_teacher_table()
        self._create_subject_table()

        self.update_shedule_button_monday = QPushButton("Update")
        self.update_shedule_button_tuesday = QPushButton("Update")
        self.update_shedule_button_wednesday = QPushButton("Update")
        self.update_shedule_button_thursday = QPushButton("Update")
        self.update_shedule_button_friday = QPushButton("Update")
        self.update_shedule_button_teacher = QPushButton("Update")
        self.update_shedule_button_subject = QPushButton("Update")
        self.svbox1.addWidget(self.update_shedule_button_monday)
        self.svbox2.addWidget(self.update_shedule_button_tuesday)
        self.svbox3.addWidget(self.update_shedule_button_wednesday)
        self.svbox4.addWidget(self.update_shedule_button_thursday)
        self.svbox5.addWidget(self.update_shedule_button_friday)
        self.svbox6.addWidget(self.update_shedule_button_teacher)
        self.svbox7.addWidget(self.update_shedule_button_subject)
        self.update_shedule_button_monday.clicked.connect(self._update_shedule)
        self.update_shedule_button_tuesday.clicked.connect(self._update_shedule)
        self.update_shedule_button_wednesday.clicked.connect(self._update_shedule)
        self.update_shedule_button_thursday.clicked.connect(self._update_shedule)
        self.update_shedule_button_friday.clicked.connect(self._update_shedule)
        self.update_shedule_button_teacher.clicked.connect(self._update_shedule)
        self.update_shedule_button_subject.clicked.connect(self._update_shedule)

        self.monday_tab.setLayout(self.svbox1)
        self.tuesday_tab.setLayout(self.svbox2)
        self.wednesday_tab.setLayout(self.svbox3)
        self.thursday_tab.setLayout(self.svbox4)
        self.friday_tab.setLayout(self.svbox5)
        self.teacher_tab.setLayout(self.svbox6)
        self.subject_tab.setLayout(self.svbox7)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()

        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(10)
        self.monday_table.setHorizontalHeaderLabels(["id", "week", "day", "number", "subject", "room numb", "start_time", "teacher_id", "", ""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()

        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(10)
        self.tuesday_table.setHorizontalHeaderLabels(["id", "week", "day", "number", "subject", "room numb", "start_time", "teacher_id", "", ""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()

        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(10)
        self.wednesday_table.setHorizontalHeaderLabels(["id", "week", "day", "number", "subject", "room numb", "start_time", "teacher_id","",""])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.mvbox)

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()

        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(10)
        self.thursday_table.setHorizontalHeaderLabels(["id", "week", "day", "number", "subject", "room numb", "start_time", "teacher_id", "", ""])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)

    def _create_friday_table(self):
        self.friday_table = QTableWidget()

        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(10)
        self.friday_table.setHorizontalHeaderLabels(["id", "week", "day", "number", "subject", "room numb", "start_time", "teacher_id", "", ""])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()

        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(5)
        self.teacher_table.setHorizontalHeaderLabels(["id", "full_name", "subject", "", ""])

        self._update_teacher_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.mvbox)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()

        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(4)
        self.subject_table.setHorizontalHeaderLabels(["id", "name", ""])

        self._update_subject_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.mvbox)

    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day=1 ORDER BY number")
        records = list(self.cursor.fetchall())
        self.monday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            joinButton1 = QPushButton("Delete")

            self.monday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.monday_table.setItem(i, 5, QTableWidgetItem(str(r[5])))
            self.monday_table.setItem(i, 6, QTableWidgetItem(str(r[6])))
            self.monday_table.setItem(i, 7, QTableWidgetItem(str(r[7])))
            self.monday_table.setCellWidget(i, 8, joinButton)
            self.monday_table.setCellWidget(i, 9, joinButton1)

            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_monday(num))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_monday(num))
        joinButton2 = QPushButton("Add")
        self.monday_table.setCellWidget(len(records), 9, joinButton2)
        joinButton2.clicked.connect(lambda: self._add_day_from_monday(len(records)))
        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 2 ORDER BY week, number")
        records = list(self.cursor.fetchall())
        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            joinButton1 = QPushButton("Delete")

            self.tuesday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.tuesday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.tuesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.tuesday_table.setItem(i, 5, QTableWidgetItem(str(r[5])))
            self.tuesday_table.setItem(i, 6, QTableWidgetItem(str(r[6])))
            self.tuesday_table.setItem(i, 7, QTableWidgetItem(str(r[7])))
            self.tuesday_table.setCellWidget(i, 8, joinButton)
            self.tuesday_table.setCellWidget(i, 9, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_tuesday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_tuesday(num))
        joinButton2 = QPushButton("Add")
        self.tuesday_table.setCellWidget(len(records), 9, joinButton2)
        joinButton2.clicked.connect(lambda: self._add_day_from_tuesday(len(records)))
        self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day=3 ORDER BY week, number")
        records = list(self.cursor.fetchall())
        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            joinButton1 = QPushButton("Delete")

            self.wednesday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.wednesday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.wednesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.wednesday_table.setItem(i, 5, QTableWidgetItem(str(r[5])))
            self.wednesday_table.setItem(i, 6, QTableWidgetItem(str(r[6])))
            self.wednesday_table.setItem(i, 7, QTableWidgetItem(str(r[7])))
            self.wednesday_table.setCellWidget(i, 8, joinButton)
            self.wednesday_table.setCellWidget(i, 9, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_wednesday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_thursday(num))
        joinButton2 = QPushButton("Add")
        self.wednesday_table.setCellWidget(len(records), 9, joinButton2)
        joinButton2.clicked.connect(lambda: self._add_day_from_wednesday(len(records)))
        self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day=4 ORDER BY week, number")
        records = list(self.cursor.fetchall())
        self.thursday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            joinButton1 = QPushButton("Delete")

            self.thursday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.thursday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.thursday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.thursday_table.setItem(i, 5, QTableWidgetItem(str(r[5])))
            self.thursday_table.setItem(i, 6, QTableWidgetItem(str(r[6])))
            self.thursday_table.setItem(i, 7, QTableWidgetItem(str(r[7])))
            self.thursday_table.setCellWidget(i, 8, joinButton)
            self.thursday_table.setCellWidget(i, 9, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_thursday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_thursday(num))
        joinButton2 = QPushButton("Add")
        self.thursday_table.setCellWidget(len(records), 9, joinButton2)
        joinButton2.clicked.connect(lambda: self._add_day_from_thursday(len(records)))
        self.thursday_table.resizeRowsToContents()

    def _update_friday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day=5 ORDER BY week, number")
        records = list(self.cursor.fetchall())
        self.friday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            joinButton1 = QPushButton("Delete")

            self.friday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.friday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.friday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.friday_table.setItem(i, 5, QTableWidgetItem(str(r[5])))
            self.friday_table.setItem(i, 6, QTableWidgetItem(str(r[6])))
            self.friday_table.setItem(i, 7, QTableWidgetItem(str(r[7])))
            self.friday_table.setCellWidget(i, 8, joinButton)
            self.friday_table.setCellWidget(i, 9, joinButton1)

            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_friday(num))
            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_friday(num))

        joinButton2 = QPushButton("Add")
        self.friday_table.setCellWidget(len(records), 9, joinButton2)
        joinButton2.clicked.connect(lambda: self._add_day_from_friday(len(records)))
        self.friday_table.resizeRowsToContents()

    def _update_teacher_table(self):
        self.cursor.execute("SELECT * FROM teacher")
        records = list(self.cursor.fetchall())
        self.teacher_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            joinButton1 = QPushButton("Delete")

            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.teacher_table.setCellWidget(i, 3, joinButton)
            self.teacher_table.setCellWidget(i, 4, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_teacher(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_teacher(num))
        joinButton2 = QPushButton("Add")
        self.teacher_table.setCellWidget(len(records), 3, joinButton2)
        joinButton2.clicked.connect(lambda: self._add_day_from_teacher(len(records)))
        self.teacher_table.resizeRowsToContents()

    def _update_subject_table(self):
        self.cursor.execute("SELECT * FROM subject")
        records = list(self.cursor.fetchall())
        self.subject_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            joinButton1 = QPushButton("Delete")

            self.subject_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.subject_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.subject_table.setCellWidget(i, 2, joinButton)
            self.subject_table.setCellWidget(i, 3, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_subject(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_subject(num))

        joinButton2 = QPushButton("Add")
        self.subject_table.setCellWidget(len(records), 3, joinButton2)
        joinButton2.clicked.connect(lambda: self._add_day_from_subject(len(records)))
        self.subject_table.resizeRowsToContents()

    def _change_day_from_monday(self, rowNum):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(f'UPDATE timetable SET week = %s, day = %s, number = %s, subject = %s, room_numb = %s, start_time = %s, teacher_id = %s WHERE id = %s;',(row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_tuesday(self, rowNum):
        row = list()
        for i in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET week = %s, day = %s, number = %s, subject = %s, room_numb = %s, start_time = %s, teacher_id = %s WHERE id = %s;",(row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_wednesday(self, rowNum):
        row = list()
        for i in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(f'UPDATE timetable SET week = %s, day = %s, number = %s, subject = %s, room_numb = %s, start_time = %s, teacher_id = %s WHERE id = %s;',(row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_thursday(self, rowNum):
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(f'UPDATE timetable SET week = %s, day = %s, number = %s, subject = %s, room_numb = %s, start_time = %s, teacher_id = %s WHERE id = %s;',(row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_friday(self, rowNum):
        row = list()
        for i in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(f'UPDATE timetable SET week = %s, day = %s, number = %s, subject = %s, room_numb = %s, start_time = %s, teacher_id = %s WHERE id = %s;',(row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_teacher(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE teacher SET full_name = %s, subject = %s WHERE id = %s;",
                (row[1], row[2], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day_from_subject(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute(f'UPDATE subject SET name = %s WHERE id = %s;', (row[0], row[1],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _del_day_from_monday(self, rowNum):
        row = list()
        for column in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s and day = 1", (row[0],))
        self.conn.commit()

    def _del_day_from_tuesday(self, rowNum):
        row = list()
        for column in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s and day = 2", (row[0],))
        self.conn.commit()

    def _del_day_from_wednesday(self, rowNum):
        row = list()
        for column in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s and day = 3", (row[0],))
        self.conn.commit()

    def _del_day_from_thursday(self, rowNum):
        row = list()
        for column in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s and day = 4", (row[0],))
        self.conn.commit()

    def _del_day_from_friday(self, rowNum):
        row = list()
        for column in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s", (row[0],))
        self.conn.commit()

    def _del_day_from_teacher(self, rowNum):
        row = list()
        for column in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM teacher WHERE id = %s", (row[0],))
        self.conn.commit()

    def _del_day_from_subject(self, rowNum):
        row = list()
        for column in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM subject WHERE id = %s", (row[1],))
        self.conn.commit()

    def _add_day_from_monday(self, rowNum):
        self.cursor.execute("INSERT INTO timetable(week, day, number, subject, room_numb, start_time, teacher_id) VALUES (0,1,0, 'Нулевой предмет', 'Введите аудиторию', 'Введите время начала', 29);")
        self.conn.commit()

    def _add_day_from_tuesday(self, rowNum):
        self.cursor.execute("INSERT INTO timetable(week, day, number, subject, room_numb, start_time, teacher_id) VALUES (0,2,0, 'Нулевой предмет', 'Введите аудиторию', 'Введите время начала', 29);")
        self.conn.commit()

    def _add_day_from_wednesday(self, rowNum):
        self.cursor.execute("INSERT INTO timetable(week, day, number, subject, room_numb, start_time, teacher_id) VALUES (0,3,0, 'Нулевой предмет', 'Введите аудиторию', 'Введите время начала', 29);")
        self.conn.commit()

    def _add_day_from_thursday(self, rowNum):
        self.cursor.execute("INSERT INTO timetable(week, day, number, subject, room_numb, start_time, teacher_id) VALUES (0,4,0, 'Нулевой предмет', 'Введите аудиторию', 'Введите время начала', 29);")
        self.conn.commit()

    def _add_day_from_friday(self, rowNum):
        self.cursor.execute("INSERT INTO timetable(week, day, number, subject, room_numb, start_time, teacher_id) VALUES (0,5,0, 'Нулевой предмет', 'Введите аудиторию', 'Введите время начала', 29);")
        self.conn.commit()

    def _add_day_from_subject(self, rowNum):
        self.cursor.execute("INSERT INTO subject(name) VALUES ('Введите предмет');")
        self.conn.commit()

    def _add_day_from_teacher(self, rowNum):
        self.cursor.execute("INSERT INTO teacher(full_name, subject) VALUES ('Введите имя преподавателя', 'Нулевой предмет');")
        self.conn.commit()

    def _update_shedule(self):
        self.conn.rollback()
        self.monday_table.setRowCount(0)
        self._update_monday_table()
        self.tuesday_table.setRowCount(0)
        self._update_tuesday_table()
        self.wednesday_table.setRowCount(0)
        self._update_wednesday_table()
        self.thursday_table.setRowCount(0)
        self._update_thursday_table()
        self.friday_table.setRowCount(0)
        self._update_friday_table()
        self.teacher_table.setRowCount(0)
        self._update_teacher_table()
        self.subject_table.setRowCount(0)
        self._update_subject_table()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())





