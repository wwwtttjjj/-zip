from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette,QBrush,QPixmap
import zipfile
import sys
class zip_file(QtWidgets.QMainWindow):
    def __init__(self):
        super(zip_file, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.resize(1000, 800)
        self.setWindowTitle("zipfile")
        self.QlineEdit_path = QLineEdit(self)
        self.QlineEdit_path.setFixedSize(500, 50)
        self.QlineEdit_path.move(200, 200)

        self.button = QPushButton(self)
        self.button.setFixedSize(50, 50)
        self.button.move(400, 300)
        self.button.setText("确定")
        self.button.clicked.connect(self.zip_filef)

    def zip_filef(self):
        filename = self.QlineEdit_path.text()
        if filename == '':
            self.remain = QMessageBox.about(self, '提示', '请输入路径')
        else:
            print(filename)
            path_list = filename.split('\\')
            save_path = '\\'.join(path_list[0:len(path_list) - 1])
            print(save_path)
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(save_path)
            self.remain = QMessageBox.about(self, '提示', '已经完成')



    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_Widnow = zip_file()
    main_Widnow.show()
    sys.exit(app.exec_())