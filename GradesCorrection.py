
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QVBoxLayout, QFileDialog


class GradesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Grades Correction")
        self.resize(750, 600)

        self.layout = QVBoxLayout()

        self.file_button = QPushButton("Select Grades File")
        self.file_button.clicked.connect(self.choose_file)
        self.layout.addWidget(self.file_button)

        self.file_label = QLabel("No file selected")
        self.layout.addWidget(self.file_label)

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def choose_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Grades File", "", "CSV Files (*.csv)"
        )

        if file_name:
            self.selected_file = file_name
            self.file_label.setText(file_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradesWindow()
    window.show()
    app.exec()
