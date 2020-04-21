from PyQt5.QtWidgets import *
from view.GUI import ApplicationWindow


class GUIController(ApplicationWindow):
    def __init__(self, code_analyzer_facade):
        ApplicationWindow.__init__(self)
        self.target_files = list()
        self.code_analyzer_facade = code_analyzer_facade
        self.vulnerability_dictionary = [
            "Уязвимость переполнения буфера в строках:",
            "Предупреждение: использование небезопасной функции (переполнение буфера): ",
            "Уязвимость ошибка форматной строки в строках:",
            "Предупреждение: использование небезопасной функции (форматная строка): ",
            "Уязвимость внедрение SQL-кода в строках",
            "Уязвимость внедрения команд в строках:",
            "Уязвимость небезопасного хранения данных в строках:",
            "Уязвимость  утечки памяти в строках: ",
            "Уязвимость некорректного доступа к файлам в строках:",
            "Уязвимость разыменования нулевого указателя в строках:",
            "Уязвимость переполнения целых чисел в строках:",
            "Уязвимость состояния гонки в строках:",
            "Уязвимость некорректной синхронизации типа читатели - писатели в стоках: ",
            "Уязвимость неинициализированных переменных в строках:"
        ]
        self.analyse_result = []

    def addFile(self):  # ф-я, которая отвечает за открытие файла
        file_path = QFileDialog.getOpenFileName(self, 'Open file', "")[0]
        if not file_path == "":
            self.file_list.addItem(str(file_path))
            source = open(file_path).readlines()
            format_source = []
            for i in range(len(source)):
                format_source.append("%2d.   %s" % (i, source[i]))
            self.target_files.append([file_path, source, format_source])
        self.showFileContent()
        pass

    def deleteFile(self):  # ф-я, которая отвечает за удаление файла (из программы)
        if self.file_list.currentRow() != -1:
            current_row = self.file_list.currentRow()
            self.file_list.takeItem(current_row)
            self.target_files.pop(current_row)
            self.code_text.setText('')
            self.code_label.setText("Листинг программы: ")
            self.file_list.setCurrentRow(-1)

    def showFileContent(self):
        row = self.file_list.currentRow()
        self.code_text.setText(''.join(self.target_files[row][2]))
        self.code_label.setText("Листинг программы: " + self.target_files[row][0])

    def generateTests(self):  # ф-я, которая отвечает за запуск генератора тестов
        self.code_analyzer_facade.generateTests()

    def analyseCode(self):  # ф-я, которая отвечает за запуск анализатора
        self.mssg_err.setText("")
        self.mssg_err.clear()
        for filename, source, format_source in self.target_files:
            self.mssg_err.append(filename + ":  ")
            self.analyse_result = self.code_analyzer_facade.get_analyse_result(self, source)

            isEmpty = True
            for i in range(len(self.analyse_result)):
                if self.analyse_result[i]:
                    isEmpty = False
                    self.mssg_err.append("  " + self.vulnerability_dictionary[i] + " " + str(self.analyse_result[i]))
            if isEmpty:
                self.mssg_err.append("  Уязвимостей выбранного типа не обнаружено")
            self.analyse_result = []
            self.mssg_err.append("")

