from model.CodeAnalyzer import *
from model.TestGenerator import *


class CodeAnalyzerFacade:
    def __init__(self):
        self.analyse_result = []

    def get_analyse_result(self, gui, source):
        analyzer = CodeAnalyzer(source)
        self.analyse_result = []

        if gui.buffer_overflow.isChecked():
            self.analyse_result.append(analyzer.search_buffer_overflow())
            self.analyse_result.append(analyzer.warn_buffer_overflow())
        else:
            self.analyse_result.append([])
            self.analyse_result.append([])

        if gui.format_string_error.isChecked():
            self.analyse_result.append(analyzer.search_format_string_error())
            self.analyse_result.append(analyzer.warn_format_string_error())
        else:
            self.analyse_result.append([])
            self.analyse_result.append([])

        if gui.sql_injection.isChecked():
            self.analyse_result.append(analyzer.search_sql_injection())
        else:
            self.analyse_result.append([])

        if gui.command_injection.isChecked():
            self.analyse_result.append(analyzer.search_command_intrusion())
        else:
            self.analyse_result.append([])

        if gui.neglecting_secure_data_storage.isChecked():
            self.analyse_result.append(analyzer.not_safe_data_store())
        else:
            self.analyse_result.append([])

        if gui.memory_leak.isChecked():
            self.analyse_result.append(analyzer.memory_leak())
        else:
            self.analyse_result.append([])

        if gui.incorrect_file_access.isChecked():
            self.analyse_result.append(analyzer.search_bad_file_access())
        else:
            self.analyse_result.append([])

        if gui.null_pointer_derefence.isChecked():
            self.analyse_result.append(analyzer.null_pointer_derefence())
        else:
            self.analyse_result.append([])

        if gui.integer_overflow.isChecked():
            self.analyse_result.append(analyzer.number_overflow())
        else:
            self.analyse_result.append([])

        if gui.incorr_race_synchr.isChecked():
            self.analyse_result.append(analyzer.search_race_condition())
        else:
            self.analyse_result.append([])

        if gui.incorr_rw_synchr.isChecked():
            self.analyse_result.append(analyzer.incorr_rw_synchr())
        else:
            self.analyse_result.append([])

        if gui.using_an_uninit_var.isChecked():
            self.analyse_result.append(analyzer.search_uninitialized_variable())
        else:
            self.analyse_result.append([])

        return self.analyse_result

    def generateTests(self):
        test_generator = TestGenerator()
        test_generator.generateTests()