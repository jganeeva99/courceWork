from PyQt5.QtWidgets import *


class ApplicationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.code_label = QLabel("Программный код:")

        self.label_file = QLabel("Путь к файлу:")
        self.add_open_file_button = QPushButton("Открыть файл")
        self.add_del_file_button = QPushButton("Удалить файл")
        self.add_gen_test_button = QPushButton("Сгенерировать тест")
        self.analyzer_button = QPushButton("Запустить анализатор")

        self.vulnerability_label = QLabel("Выберите уязвимость/уязвимости:")
        self.buffer_overflow = QCheckBox("Переполнение буфера")
        self.format_string_error = QCheckBox("Ошибка форматной строки")
        self.sql_injection = QCheckBox("Внедрение SQL-кода")
        self.command_injection = QCheckBox("Внедрение команд")
        self.neglecting_secure_data_storage = QCheckBox("Пренебрежение безопасным хранением данных")
        self.memory_leak = QCheckBox("Утечка памяти")
        self.incorrect_file_access = QCheckBox("Некорректный доступ к файлу")
        self.null_pointer_derefence = QCheckBox("Разыменование нулевого указателя")
        self.integer_overflow = QCheckBox("Переполнние целых чисел")
        self.incorr_race_synchr = QCheckBox("Некорректная синхронизация типа гонки")
        self.incorr_rw_synchr = QCheckBox("Некорректная синхронизация типа читатели-писатели")
        self.using_an_uninit_var = QCheckBox("Использование неинициализированной переменной")

        self.vulnerability_out = QLabel("Выявленные уязвимости:")

        self.initUI()

    def initUI(self):
        QWidget.__init__(self, parent=None)
        self.setWindowTitle("Статический анализатор уязвимостей кода на языке С++")
        self.resize(1000, 1000)

        # часть для вывода кода
        layout = QWidget();
        self.code_text = QTextEdit()
        self.code_text.setReadOnly(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.code_label)
        self.layout.addWidget(self.code_text)

        # чекбоксы
        self.cheсk_layout = QVBoxLayout()
        self.cheсk_layout.addWidget(self.vulnerability_label)
        self.cheсk_layout.addWidget(self.buffer_overflow)
        self.cheсk_layout.addWidget(self.format_string_error)
        self.cheсk_layout.addWidget(self.sql_injection)
        self.cheсk_layout.addWidget(self.command_injection)
        self.cheсk_layout.addWidget(self.neglecting_secure_data_storage)
        self.cheсk_layout.addWidget(self.memory_leak)
        self.cheсk_layout.addWidget(self.incorrect_file_access)
        self.cheсk_layout.addWidget(self.null_pointer_derefence)
        self.cheсk_layout.addWidget(self.integer_overflow)
        self.cheсk_layout.addWidget(self.incorr_race_synchr)
        self.cheсk_layout.addWidget(self.incorr_rw_synchr)
        self.cheсk_layout.addWidget(self.using_an_uninit_var)

        # кнопки открыть файл/ удалить файл / сгенерировать тест / запустить анализатор
        self.file_list = QListWidget()
        self.file_list.clicked.connect(self.showFileContent)
        self.butt = QVBoxLayout()

        self.butt.addWidget(self.label_file)
        self.butt.addWidget(self.file_list)
        self.butt.addWidget(self.add_open_file_button)
        self.butt.addWidget(self.add_del_file_button)
        self.butt.addWidget(self.add_gen_test_button)
        self.butt.addWidget(self.analyzer_button)

        # вывод выявленных уязвимости
        self.mssg_err = QTextEdit()
        self.mssg_err.setReadOnly(True)
        self.err_out = QVBoxLayout()
        self.err_out.addWidget(self.vulnerability_out)
        self.err_out.addWidget(self.mssg_err)

        # объединение виджетов
        self.first = QVBoxLayout()
        self.first.addLayout(self.butt)
        self.first.addLayout(self.cheсk_layout)

        self.second = QHBoxLayout()
        self.second.addLayout(self.first)
        self.second.addLayout(self.layout)

        self.third = QVBoxLayout()
        self.third.addLayout(self.second)
        self.third.addLayout(self.err_out)
        self.setLayout(self.third)

        self.add_open_file_button.clicked.connect(self.addFile)
        self.add_del_file_button.clicked.connect(self.deleteFile)
        self.add_gen_test_button.clicked.connect(self.generateTests)
        self.analyzer_button.clicked.connect(self.analyseCode)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы действительно хотите закрыть приложение?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def addFile(self):  # ф-я, которая отвечает за открытие файла
        pass

    def deleteFile(self):  # ф-я, которая отвечает за удаление файла (из программы)
        pass

    def generateTests(self):  # ф-я, которая отвечает за запуск генератора тестов
        pass

    def analyseCode(self):  # ф-я, которая отвечает за запуск анализатора
        pass