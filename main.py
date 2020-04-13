from view.GUIController import *
from model.CodeAnalyzerFacade import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui_controller = GUIController(CodeAnalyzerFacade())

    sys.exit(app.exec_())