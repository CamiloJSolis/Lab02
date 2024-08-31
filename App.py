import sys
from PyQt6.QtWidgets import (QMainWindow, QLineEdit, QPushButton, QMessageBox,
                             QPlainTextEdit, QApplication, QFileDialog)
from PyQt6.uic import loadUi
from urllib3.util import current_time


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("MainGUI.ui", self)

        #Defining widgets
        self.save_button = self.findChild(QPushButton, "btn_grabar")
        self.path_button = self.findChild(QPushButton, "btn_ruta")
        self.obtain_button = self.findChild(QPushButton, "btn_obtener")
        self.exit_button = self.findChild(QPushButton, "btn_salir")

        self.name_plain_text_edit = self.findChild(QPlainTextEdit, "pTEd_nombre")
        self.surname_plain_text_edit = self.findChild(QPlainTextEdit, "pTEd_apellido")

        self.path_line_edit = self.findChild(QLineEdit, "lnEd_ruta")
        self.data_line_edit = self.findChild(QLineEdit, "lnEd_dato")

        #Buttons actions
        self.save_button.clicked.connect(self.save_button_clicked)
        self.path_button.clicked.connect(self.path_button_clicked)
        self.exit_button.clicked.connect(self.exit_button_click)
        self.obtain_button.clicked.connect(self.obtain_button_clicked)
        self.data = ""

    def path_button_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "Text Files (*.txt)")
        if file_name:
            try:
                with open(file_name, "r") as f:
                    self.data = f.read()
                    self.path_line_edit.setText(file_name)
            except Exception as ex:
                QMessageBox.critical(self, "Abrir Archivo", f"Ocurrió un error al abrir el archivo: {ex}")

    def save_button_clicked(self):
        try:
            save_file, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Text Files (*.txt)")
            if save_file:
                f = open(save_file, "a")
                with f:
                    try:
                        text = self.data_line_edit.text()
                        f.write(f"{text}\n")

                        QMessageBox.about(self, "Guardar Archivo", "Archivo guardado exitosamente")
                        clear_name_field = self.name_plain_text_edit
                        clear_surname_field = self.surname_plain_text_edit
                        clear_path_field = self.path_line_edit
                        clear_data_field = self.data_line_edit

                        clear_name_field.clear()
                        clear_surname_field.clear()
                        clear_path_field.clear()
                        clear_data_field.clear()
                    except Exception as ex:
                        QMessageBox.critical(self, "Guardar Archivo", f"Ocurrió un error al guardar el archivo: {ex}")
        except Exception as ex:
            QMessageBox.critical(self, "Guardar Archivo", f"Ocurrió un error en el proceso de guardardado del archivo: {ex}")

    def exit_button_click(self):
        try:
            confirm = QMessageBox.question(self, "Confirmación de salida", "¿Está seguro que desea salir?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.close()
        except Exception as ex:
            QMessageBox.critical(self, "Cerrar aplicación", f"Ocurrió un error al cerrar el programa {ex}")

    def obtain_button_clicked(self):
        try:
            clear_name_field = self.name_plain_text_edit
            clear_surname_field = self.surname_plain_text_edit

            clear_name_field.clear()
            clear_surname_field.clear()

            data = self.data
            lines  = data.split("\n")

            for line in lines:
                comma_separation = line.split(",")
                if len(comma_separation) == 2:
                    name = comma_separation[0]
                    surname = comma_separation[1]

                    current_name = self.name_plain_text_edit.toPlainText()
                    current_surname = self.surname_plain_text_edit.toPlainText()

                    self.name_plain_text_edit.setPlainText(current_name + name + "\n")
                    self.surname_plain_text_edit.setPlainText(current_surname + surname + "\n")
        except Exception as ex:
            QMessageBox.critical(self, "Obtener Datos", f"Ocurrió un error al mostrar los datos: {ex}")

def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()

    try:
        app.exec()
    except Exception as ex:
        QMessageBox.critical("Error", f"Ocurrió un error al ejecutar la aplicación: {ex}")


main()