# Estilo principal da janela (fundo, fontes, botões, campos de texto)
EVENT_STYLE = """
QWidget {
    background-color: #1e1e1e;  /* Fundo escuro estilo Apple */
    color: #f0f0f0;  /* Cor do texto clara */
    font-family: 'Helvetica Neue', Arial, sans-serif;  /* Fonte moderna e limpa */
    font-size: 15px;  /* Tamanho padrão da fonte */
}

QPushButton {
    background-color: #2c2c2e;  /* Botão com cinza escuro elegante */
    color: white;  /* Texto branco no botão */
    padding: 10px 20px;  /* Espaçamento interno confortável */
    border-radius: 10px;  /* Borda arredondada estilo Apple */
    font-weight: bold;  /* Texto em negrito */
}

QPushButton:hover {
    background-color: #3a3a3c;  /* Cor mais clara ao passar o mouse */
}

QLineEdit {
    background-color: #2a2a2a;  /* Campo de texto escuro */
    color: white;  /* Texto branco no campo */
    border: 1px solid #444;  /* Borda discreta */
    border-radius: 8px;  /* Borda arredondada */
    padding: 6px;  /* Espaçamento interno */
    font-size: 14px;  /* Tamanho do texto nos campos */
}
"""

# Estilo da tabela de eventos
TABELA_STYLE = """
QTableWidget {
    background-color: #1e1e1e;  /* Fundo da tabela */
    color: #f0f0f0;  /* Texto padrão */
    gridline-color: #333;  /* Cor das linhas da grade */
    font-size: 14px;  /* Tamanho da fonte nas células */
    border: none;  /* Remove bordas externas */
}

QHeaderView::section {
    background-color: #2c2c2e;  /* Cabeçalho da tabela em tom escuro */
    color: #ffffff;  /* Texto branco no cabeçalho */
    font-weight: bold;  /* Negrito para destacar */
    padding: 8px;  /* Espaçamento interno */
    border: none;  /* Sem borda */
}

QTableWidget::item {
    padding: 8px;  /* Espaçamento interno nas células */
    border: none;  /* Sem borda nas células */
}

QTableWidget::item:selected {
    background-color: #444;  /* Destaque da linha selecionada */
}
"""
