# src/ui/main_styles.py

MAIN_STYLE = """
    QWidget {
        background-color: #1e1e1e;
        color: #f0f0f0;
        font-family: "Helvetica Neue", Arial, sans-serif;
        font-size: 14px;
    }

    QLabel {
        font-size: 18px;
        font-weight: bold;
        padding: 6px;
    }

    QScrollArea {
        border: none;
    }

    QLineEdit {
        background-color: #2c2c2e;
        color: white;
        border: 1px solid #3a3a3c;
        border-radius: 6px;
        padding: 6px;
    }
"""

BOTAO_STYLE = """
    QPushButton {
        background-color: #2c2c2e;
        color: white;
        padding: 8px 16px;
        border: none;
        border-radius: 8px;
        font-weight: 500;
    }

    QPushButton:hover {
        background-color: #3a3a3c;
    }

    QPushButton:disabled {
        background-color: #444;
        color: #999;
    }
"""

FRAME_STYLE = """
    QFrame {
        background-color: #2a2a2a;
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 15px;
    }
"""

IMAGEM_STYLE = """
    QLabel {
        border-radius: 10px;
        margin: 4px;
    }
"""
