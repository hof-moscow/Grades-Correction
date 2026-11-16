
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QVBoxLayout, QFileDialog,QSpinBox,QTableWidgetItem


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
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 180)
        self.layout.addWidget(self.table)

        # Bonus points
        self.bonus_label = QLabel("Bonus Points:")
        self.layout.addWidget(self.bonus_label)

        self.bonus_input = QSpinBox()
        self.bonus_input.setRange(0, 100)
        self.bonus_input.setSuffix(" points")
        self.bonus_input.editingFinished.connect(self.apply_bonus)
        self.layout.addWidget(self.bonus_input)

        # Update file button
        self.update_button = QPushButton("Update File")
        self.update_button.clicked.connect(self.update_file)
        self.layout.addWidget(self.update_button)

        # Status message
        self.status_label = QLabel("Select a file to begin")
        self.layout.addWidget(self.status_label)


        self.setLayout(self.layout)
        with open("style.qss", "r") as f:
            self.setStyleSheet(f.read())

    
    def choose_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Grades File", "", "CSV Files (*.csv)"
        )

        if file_name:
            self.selected_file = file_name
            self.file_label.setText(file_name)

            self.student_ids = []
            self.original_grades = []
            self.corrected_grades = []

            with open(file_name, "r") as f:
                next(f) 

                for line in f:
                    student_id, grade = line.strip().split(",")

                    self.student_ids.append(student_id)
                    self.original_grades.append(int(grade))
                    self.corrected_grades.append(int(grade))

            self.bonus_input.setValue(0)
            self.update_table()
            self.status_label.setText("File loaded successfully")


    def update_table(self):
        self.table.clearContents()

        for i in range(len(self.student_ids)):
            self.table.setItem(i, 0, QTableWidgetItem(self.student_ids[i]))
            self.table.setItem(i, 1, QTableWidgetItem(str(self.original_grades[i])))
            self.table.setItem(i, 2, QTableWidgetItem(str(self.corrected_grades[i])))


    def apply_bonus(self):
        self.status_label.setText("Bonus entered. Grades not updated yet.")

    def update_file(self):
        self.status_label.setText("File update is not implemented yet.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradesWindow()
    window.show()
    app.exec()
