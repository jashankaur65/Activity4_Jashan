from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QMessageBox, QVBoxLayout, QWidget, QTableWidgetItem, QComboBox
from PySide6.QtCore import Slot
from to_do_list.task_editor import TaskEditor
import csv
import os

class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initialize_widgets()
        self.__connect_signals()

    def __initialize_widgets(self):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("To-Do List")

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("New Task")

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])

        self.add_button = QPushButton("Add Task", self)

        self.save_button = QPushButton("Save to CSV", self)
        

        self.task_table = QTableWidget(self)
        self.task_table.setColumnCount(2)
        self.task_table.setHorizontalHeaderLabels(["Task", "Status"])


        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.task_input)
        layout.addWidget(self.status_combo)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_table)
        layout.addWidget(self.save_button)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def __connect_signals(self):
        """
        Connects signals to their respective slots.
        """
        self.add_button.clicked.connect(self.on_add_task)
        self.save_button.clicked.connect(self.__save_to_csv)

    @Slot()
    def on_add_task(self):
        task = self.task_input.text()
        status = self.status_combo.currentText()

        if len(task.strip()) > 0:
            row_position = self.task_table.rowCount()
            self.task_table.insertRow(row_position)
            self.task_table.setItem(row_position, 0, QTableWidgetItem(task))
            self.task_table.setItem(row_position, 1, QTableWidgetItem(status))
            self.status_label.setText(f"Added task: {task}")

        else:
            self.status_label.setText("Please enter a task and select its status.")

    @Slot()
    def on_edit_task(self,row):
        current_status = self.task_table.item(row, 1).text()
        task_editor = TaskEditor(row, current_status)
        task_editor.task_updated.connect(self.update_task_status)
        task_editor.exec()

    @Slot(int, str)
    def update_task_status(self,row,new_status):
        self.task_table.setItem(row, 1, QTableWidgetItem(new_status))
        self.status_label.setText(f"Task status updated to: {new_status}")
    # Part 3
    def __load_data(self, file_path: str):
        """
        Reads data from the .csv file provided.
        Calls the __add_table_row method (to be implemented) 
        for each row of data.
        Args:
            file_path (str): The name of the file (including relative path).
        """
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row
            header = next(reader)  
            for row in reader:
                self.__add_table_row(row)
    
    def __add_table_row(self, row_data):
        """
        Remove the pass statement below to implement this method.
        """
        row_position = self.task_table.rowCount()
        self.task_table.insertRow(row_position)
        self.task_table.setItem(row_position, 0, QTableWidgetItem(row_data[0]))
        self.task_table.setItem(row_position, 1, QTableWidgetItem(row_data[1]))
    
    def __save_to_csv(self):
        """
        Saves the QTable data to a file.
        """
        file_path = 'output/todos.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(["Task", "Status"])
            for row in range(self.task_table.rowCount()):
                task = self.task_table.item(row, 0).text()
                status = self.task_table.item(row, 1).text()
                writer.writerow([task, status])