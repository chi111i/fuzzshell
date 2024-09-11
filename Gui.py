from PySide6 import QtCore, QtWidgets
import sys
from ui_untitledzisi import Ui_Form
import shellmain
import phpinfo
from fenjing import exec_cmd_payload

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("fuzzshell by chi11i")
        
        self.emitter = EmittingStr()
        self.emitter.textWritten.connect(self.ui.textBrowser.append)
        self.ui.textBrowser.setReadOnly(False)
        sys.stdout = self.emitter
        sys.stderr = self.emitter

        self.ui.pushButton.clicked.connect(self.on_button_clicked)
        self.ui.pushButton_2.clicked.connect(self.remove_duplicates)
        self.ui.pushButton_3.clicked.connect(self.ui.textBrowser.clear)
        self.ui.pushButton_4.clicked.connect(self.filter_blacklist)
        self.ui.pushButton_5.clicked.connect(self.copy_text_browser)

    def copy_text_browser(self):
        self.ui.textBrowser.selectAll()
        self.ui.textBrowser.copy()

    @QtCore.Slot()
    def on_button_clicked(self):
        shell = self.ui.lineEdit.text()
        if self.ui.checkBox.isChecked():
            shellmain.shellpro(shell)
        if self.ui.checkBox_2.isChecked():
            shellmain.readfilepro(shell)
            shellmain.readfilepro(shellmain.re_string(shell))
        if self.ui.checkBox_3.isChecked():
            print(shellmain.str_to_oct(shell))
        if self.ui.checkBox_4.isChecked():
            print(shellmain.str_to_hex(shell))
        if self.ui.checkBox_5.isChecked():
            print(shellmain.ip_to_int(shell))
        if self.ui.checkBox_6.isChecked():
            shellmain.readfilebata(shell)
        if self.ui.checkBox_7.isChecked():
            print(shellmain.php_readfile(shell))
        if self.ui.checkBox_8.isChecked():
            print(shellmain.php_shell(shell))
        if self.ui.checkBox_9.isChecked():
            black_list = self.get_blacklist()
            print(shellmain.python_shell(shell, black_list))
        if self.ui.checkBox_10.isChecked():
            black_list = self.get_blacklist()
            self.set_global_variable("blacklist", black_list)
            self.ssti_shell(shell)
        if self.ui.checkBox_11.isChecked():
            html_content = self.ui.lineEdit.text()
            phpinfo.phpinfo = phpinfo.Phpinfo(html_content)
            phpinfo.phpinfo.resolvePhpinfo()
            phpinfo.phpinfo.resolveRules()
            phpinfo.phpinfo.prinRes()

    def remove_duplicates(self):
        lines = self.ui.textBrowser.toPlainText().splitlines()
        unique_lines = set(lines)
        self.ui.textBrowser.clear()
        for line in unique_lines:
            self.ui.textBrowser.append(line)

    @QtCore.Slot()
    def filter_blacklist(self):
        blacklist = self.ui.lineEdit_2.text().split(",")
        lines = self.ui.textBrowser.toPlainText().splitlines()
        filtered_lines = [line for line in lines if not any(black_item in line for black_item in blacklist)]
        self.ui.textBrowser.clear()
        for line in filtered_lines:
            self.ui.textBrowser.append(line)

    def get_blacklist(self):
        return self.ui.lineEdit_2.text().split(",")

    def set_global_variable(self, var_name, var_value):
        globals()[var_name] = var_value

    def waf(self, s: str):
        blacklist = globals()['blacklist']
        return all(word not in s for word in blacklist)

    def ssti_shell(self, shell):
        shell_payload, will_print = exec_cmd_payload(self.waf, shell)
        if not will_print:
            print("无法生成payload")
        print(f"{shell_payload=}")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
