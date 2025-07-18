from PySide6.QtWidgets import  QPushButton,  QVBoxLayout,  QComboBox, QDialog
from PySide6.QtCore import Signal

class TaskEditor(QDialog):
    task_updated = Signal(int, str)

    def __init__(self, row: int, status: str):
        super().__init__()
        self.row = row
        self.initialize_widgets(row, status)
        self.connect_signals()


    def initialize_widgets(self, row: int, status: str):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("Edit Task Status")

        self.row = row

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])
        

        self.save_button = QPushButton("Save", self)


        layout = QVBoxLayout()
        layout.addWidget(self.status_combo)
        layout.addWidget(self.save_button)
        self.setLayout(layout)
        self.setFixedWidth(150)

    def connect_signals(self):
        """
        Connects signals to appropriate slots.
        """
        self.save_button.clicked.connect(self.on_save)

    def on_save(self):
        """
        Slot triggered when save button is clicked. Emits the task_updated signal with the row and selected status.
        """
        new_status = self.status_combo.currentText()
        self.task_updated.emit(self.row, new_status)
        self.accept()