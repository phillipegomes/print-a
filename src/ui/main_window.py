        for idx, caminho in enumerate(imagens):
            thumb = QPixmap(caminho).scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            nome = os.path.basename(caminho)
            contagem = self.print_counter.get_contagem(caminho)

            img_label = QLabel()
            img_label.setPixmap(thumb)
            img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            img_label.setStyleSheet("border-radius: 8px;")

            contador_label = QLabel(f"Impresso: {contagem}/{self.limite_copias}")
            contador_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            contador_label.setStyleSheet("font-size: 11px; color: #888; margin-top: 4px;")

            spin = QSpinBox()
            spin.setMinimum(1)
            spin.setMaximum(self.limite_copias)
            spin.setValue(1)
            spin.setFixedWidth(50)
            spin.setStyleSheet("padding: 2px; font-size: 11px;")

            btn_imprimir = QPushButton("Imprimir")
            btn_imprimir.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_imprimir.setStyleSheet("font-size: 11px; padding: 4px;")
            btn_imprimir.clicked.connect(lambda _, c=caminho, s=spin, l=contador_label: self.acao_imprimir(c, s.value(), l))

            btn_excluir = QPushButton("Excluir")
            btn_excluir.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_excluir.setStyleSheet("font-size: 11px; padding: 4px;")
            btn_excluir.clicked.connect(lambda _, c=caminho: self.acao_excluir(c))

            btn_whatsapp = QPushButton("WhatsApp")
            btn_whatsapp.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_whatsapp.setStyleSheet("font-size: 11px; padding: 4px;")
            btn_whatsapp.clicked.connect(lambda _, c=caminho: self.acao_whatsapp(c))

            botoes = QHBoxLayout()
            botoes.setSpacing(4)
            botoes.addWidget(btn_imprimir)
            botoes.addWidget(spin)
            botoes.addWidget(btn_whatsapp)
            botoes.addWidget(btn_excluir)

            caixa = QVBoxLayout()
            caixa.setSpacing(4)
            caixa.setContentsMargins(6, 6, 6, 6)
            caixa.addWidget(img_label)
            caixa.addWidget(contador_label)
            caixa.addLayout(botoes)

            container = QWidget()
            container.setLayout(caixa)
            container.setStyleSheet(\"""
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 12px;
                padding: 6px;
                margin: 8px;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
            \""")

            self.grid.addWidget(container, idx // 3, idx % 3, alignment=Qt.AlignmentFlag.AlignCenter)
