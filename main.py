import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from theme import apply_dark_theme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_dark_theme(app)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
