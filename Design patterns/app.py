import sys, re
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ui import Ui_Form
import converter





## Program main function
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

## Contains logic of UI elements (actions), calls UiForm to draw a window 
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def btn_locate_file_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None,"Select file", "",filter="*.txt",selectedFilter="*.txt", options=options)
        if fileName:
            self.ui.textEdit.setText(fileName)
    
    def btn_locate_folder_clicked(self):
        options = QFileDialog.Options()
        file = QFileDialog.getSaveFileName(None, "New file name and folder", filter = "csv (*.csv);;xml (*.xml)",options=options )
        if file :
            self.ui.textEdit_2.setText(file[0])

    def rbtn_tocsv_clicked(self):
        self.ui.rbtn_toxml.setChecked(False)

    def rbtn_toxml_clicked(self):
        self.ui.rbtn_tocsv.setChecked(False)


    def btn_convert_clicked(self):
        origin = self.ui.textEdit.text()
        target = self.ui.textEdit_2.text()
        if origin and target:
            try:
                if self.ui.rbtn_tocsv.isChecked():
                    if ".csv" not in target:
                        target = target + ".csv"
                    converter.TxtToCsv(origin, target).convert()
                elif self.ui.rbtn_toxml.isChecked():
                    if ".xml" not in target:
                        target = target + ".xml"
                    converter.TxtToXml(origin, target).convert()
                dlg = QMessageBox()
                dlg.setText("Conversion is Done\nPlease check output location.")
                dlg.setWindowTitle("Something went wrong!")
                dlg.exec()
            except Exception:
                dlg = QMessageBox()
                dlg.setText("Error during file processing\nPlease check if selected files is correct.")
                dlg.setWindowTitle("Something went wrong!")
                dlg.exec()

        

if __name__ == "__main__":
    main()
