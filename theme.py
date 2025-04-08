# Copyright © 2025 Mr Ciphers. All rights reserved.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

def apply_dark_theme(app: QApplication):
    app.setStyleSheet("""
        QWidget {
            background-color: #0b0f14;
            color: #00ff99;
            font-family: 'Fira Code', Consolas, monospace;
            font-size: 13px;
        }

        QLabel {
            font-weight: bold;
            font-size: 15px;
            color: #00ff99;
        }

        QGroupBox {
            border: 1.5px solid #00ff99;
            border-radius: 12px;
            margin-top: 18px;
            padding: 20px;
            background-color: #101820;
        }

        QGroupBox:title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 10px;
            font-weight: bold;
            font-size: 17px;
            color: #00ffcc;
        }

        QPushButton {
            background-color: #0f1a1a;
            color: #00ffcc;
            padding: 12px 20px;
            font-weight: bold;
            font-family: 'Fira Code', Consolas, monospace;
            font-size: 14px;
            border: 2px solid #00ffcc;
            border-radius: 8px;
        }

        QPushButton:hover {
            background-color: #1a2a2a;
        }

        QPushButton:pressed {
            background-color: #223333;
        }

        QTextEdit {
            background-color: #000000;
            color: #00ff66;
            font-family: 'Fira Code', Consolas, monospace;
            font-size: 13px;
            border: 1px solid #00ff99;
            border-radius: 10px;
            padding: 10px;
        }

        QLineEdit {
            background-color: #1a1a1a;
            border: 1px solid #00ff99;
            padding: 8px;
            border-radius: 8px;
            color: #00ffcc;
            font-family: 'Fira Code', Consolas, monospace;
        }

        QTabWidget::pane {
            border: 1.5px solid #00ff99;
            border-radius: 12px;
            background-color: #121b22;
        }

        QTabBar::tab {
            background: #081018;
            color: #00ffcc;
            border: 1px solid #00ffcc;
            padding: 12px 28px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            margin-right: 2px;
            font-size: 14px;
        }

        QTabBar::tab:selected {
            background: #112233;
            color: #39e9bb;
            font-weight: bold;
        }

        #FooterLabel {
            color: #666;
            font-size: 12px;
            padding: 8px;
            border-top: 1px solid #333;
        }
    """)

def add_footer(widget: QWidget):
    footer = QLabel("© 2025 Mr Ciphers. All rights reserved.")
    footer.setAlignment(Qt.AlignCenter)
    footer.setObjectName("FooterLabel")

    layout = widget.layout()
    if layout:
        layout.addWidget(footer)
    else:
        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(footer)
        container = QWidget()
        container.setLayout(layout)
        return container

    return widget