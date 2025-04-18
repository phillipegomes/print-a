# src/ui/event_styles.py
# Estilos visuais para a tela de eventos (estilo Apple-like, minimalista)

def aplicar_estilo_eventos(widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #f8f8f8;
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
            color: #333;
        }

        QListWidget {
            background-color: #ffffff;
            border: 1px solid #ddd;
            padding: 5px;
        }

        QListWidget::item {
            padding: 10px;
            border-bottom: 1px solid #eee;
        }

        QListWidget::item:selected {
            background-color: #e0f0ff;
            color: #000;
            border: none;
        }

        QPushButton {
            background-color: #eaeaea;
            border: 1px solid #ccc;
            border-radius: 6px;
            padding: 8px 16px;
            min-width: 80px;
        }

        QPushButton:hover {
            background-color: #d4eaff;
            border: 1px solid #7abaff;
        }

        QLineEdit {
            padding: 6px;
            border: 1px solid #ccc;
            border-radius: 4px;
            background: white;
        }

        QLabel {
            font-weight: bold;
            margin-right: 6px;
        }
    """)
