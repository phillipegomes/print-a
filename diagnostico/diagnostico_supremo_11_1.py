"""
🧠 Diagnóstico Supremo Final 11.1 – Análise Completa de Software
Descrição: Diagnóstico universal para qualquer software, verificando todas as categorias de erros
(interpretação, estrutura, código, funcionalidades, segurança, UX, testes, documentação, manutenção,
conformidade, desempenho, integrações). Gera um relatório detalhado com erro, causa, impacto, correção,
e severidade. Otimizado para ChatGPT, simulando ferramentas sem subprocessos.
Gerado em: 2025-04-20
"""

import os
import re
import ast
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple
from PIL import Image

# Configurações
PROJETO = Path(__file__).resolve().parent.parent
RELATORIO_PATH = PROJETO / "diagnostico" / "diagnosticos"
RELATORIO_PATH.mkdir(parents=True, exist_ok=True)
NOME_RELATORIO = f"relatorio_diagnostico_supremo_11_1_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
ARQUIVO_RELATORIO = RELATORIO_PATH / NOME_RELATORIO

log: List[str] = []
erros: List[Dict[str, str]] = []

def logar(msg: str) -> None:
    """Adiciona uma mensagem ao log e imprime."""
    print(msg)
    log.append(msg)

def registrar_erro(categoria: str, erro: str, causa: str, impacto: str, correcao: str, severidade: str) -> None:
    """Registra um erro com detalhes."""
    erros.append({
        "categoria": categoria,
        "erro": erro,
        "causa": causa,
        "impacto": impacto,
        "correcao": correcao,
        "severidade": severidade
    })

def verificar_estrutura_basica() -> None:
    """Verifica a estrutura básica do projeto."""
    logar("\n📂 Verificando estrutura básica do projeto...")
    pastas_esperadas = ["src", "tests", "docs"]
    arquivos_esperados = ["README.md", ".gitignore"]

    for pasta in pastas_esperadas:
        path = PROJETO / pasta
        if not path.exists():
            registrar_erro(
                "Estrutura",
                f"Pasta '{pasta}' ausente",
                "Estrutura padrão não seguida",
                "Dificulta organização e manutenção",
                f"Criar pasta '{pasta}' com conteúdo relevante",
                "Média"
            )
        else:
            logar(f"✅ Pasta '{pasta}' presente")

    for arquivo in arquivos_esperados:
        path = PROJETO / arquivo
        if not path.exists():
            registrar_erro(
                "Estrutura",
                f"Arquivo '{arquivo}' ausente",
                "Arquivos essenciais não incluídos",
                "Dificulta instalação ou colaboração",
                f"Criar '{arquivo}' com conteúdo padrão",
                "Média"
            )
        else:
            logar(f"✅ Arquivo '{arquivo}' presente")

def verificar_funcionalidades(requisitos: List[str]) -> None:
    """Verifica se as funcionalidades solicitadas estão implementadas."""
    logar("\n🔍 Verificando funcionalidades...")
    for req in requisitos:
        encontrado = False
        for path in (PROJETO / "src").rglob("*"):
            if path.suffix in [".py", ".js"]:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        if req.lower() in f.read().lower():
                            encontrado = True
                            break
                except Exception as e:
                    registrar_erro(
                        "Funcionalidades",
                        f"Erro ao analisar {path}",
                        f"Falha na leitura: {e}",
                        "Impossível verificar funcionalidade",
                        "Verificar permissões do arquivo",
                        "Média"
                    )
        if not encontrado:
            registrar_erro(
                "Funcionalidades",
                f"Funcionalidade '{req}' não implementada",
                "Requisito não encontrado no código",
                "Funcionalidade essencial ausente",
                f"Implementar '{req}' no código",
                "Alta"
            )
        else:
            logar(f"✅ Funcionalidade '{req}' parece estar implementada")

def verificar_codigo() -> None:
    """Verifica sintaxe, lógica e padrões de código via AST."""
    logar("\n📜 Verificando código...")
    for path in (PROJETO / "src").rglob("*"):
        if path.suffix == ".py":
            try:
                with open(path, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                    tree = ast.parse(conteudo)
                # Verificar variáveis não usadas
                for node in ast.walk(tree):
                    if isinstance(node, ast.Name) and node.id.startswith("_"):
                        registrar_erro(
                            "Código",
                            f"Variável não usada '{node.id}' em {path}",
                            "Padrão de codificação não seguido",
                            "Pode indicar lógica incompleta",
                            "Remover variável ou usá-la",
                            "Baixa"
                        )
                logar(f"✅ {path} analisado via AST")
            except SyntaxError as e:
                registrar_erro(
                    "Código",
                    f"Erro de sintaxe em {path}",
                    f"Sintaxe inválida: {e}",
                    "Código não executável",
                    "Corrigir sintaxe no trecho indicado",
                    "Alta"
                )
            except Exception as e:
                registrar_erro(
                    "Código",
                    f"Erro ao analisar {path}",
                    f"Falha na análise: {e}",
                    "Impossível verificar código",
                    "Verificar formato do arquivo",
                    "Média"
                )

def verificar_seguranca() -> None:
    """Verifica vulnerabilidades de segurança."""
    logar("\n🔒 Verificando segurança...")
    padroes_inseguros = {
        r"password\s*=\s*['\"][^'\"]+['\"]": ("Senhas hardcoded", "Exposição de credenciais", "Usar variáveis de ambiente"),
        r"eval\s*\(": ("Uso de eval", "Risco de injeção de código", "Substituir por alternativas seguras"),
        r"app\.route\s*\(.*methods\s*=\s*\[['\"](GET|POST)['\"]\]": ("Falta de validação CSRF", "Vulnerabilidade a ataques CSRF", "Adicionar proteção CSRF")
    }

    for path in (PROJETO / "src").rglob("*"):
        if path.suffix in [".py", ".js"]:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                for padrao, (erro, impacto, correcao) in padroes_inseguros.items():
                    if re.search(padrao, conteudo):
                        registrar_erro(
                            "Segurança",
                            erro,
                            "Prática insegura detectada",
                            impacto,
                            correcao,
                            "Alta"
                        )
                        logar(f"❌ {erro} em {path}")
                logar(f"✅ {path} verificado para segurança")
            except Exception as e:
                registrar_erro(
                    "Segurança",
                    f"Erro ao analisar {path}",
                    f"Falha na leitura: {e}",
                    "Impossível verificar segurança",
                    "Verificar permissões do arquivo",
                    "Média"
                )

def verificar_usabilidade() -> None:
    """Verifica usabilidade e UX/UI."""
    logar("\n🎨 Verificando usabilidade e UX/UI...")
    for path in (PROJETO / "templates").rglob("*.html"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                conteudo = f.read()
            if "alt=" not in conteudo:
                registrar_erro(
                    "Usabilidade",
                    f"Imagens sem texto alternativo em {path}",
                    "Falta de atributos de acessibilidade",
                    "Inacessível para leitores de tela",
                    "Adicionar atributos alt em todas as imagens",
                    "Média"
                )
            if "aria-" not in conteudo:
                registrar_erro(
                    "Usabilidade",
                    f"Falta de atributos ARIA em {path}",
                    "Falta de suporte a acessibilidade",
                    "Dificulta uso por usuários com deficiência",
                    "Adicionar atributos ARIA apropriados",
                    "Média"
                )
            logar(f"✅ {path} verificado para usabilidade")
        except Exception as e:
            registrar_erro(
                "Usabilidade",
                f"Erro ao analisar {path}",
                f"Falha na leitura: {e}",
                "Impossível verificar usabilidade",
                "Verificar formato do arquivo",
                "Média"
            )

def verificar_testes() -> None:
    """Verifica a presença e qualidade dos testes."""
    logar("\n🧪 Verificando testes...")
    tests_path = PROJETO / "tests"
    if not tests_path.exists():
        registrar_erro(
            "Testes",
            "Pasta 'tests' ausente",
            "Falta de testes automatizados",
            "Bugs podem passar despercebidos",
            "Criar pasta 'tests' com testes unitários",
            "Alta"
        )
        return
    test_files = list(tests_path.rglob("test_*.py"))
    if not test_files:
        registrar_erro(
            "Testes",
            "Nenhum arquivo de teste encontrado",
            "Falta de testes automatizados",
            "Bugs podem passar despercebidos",
            "Adicionar arquivos de teste com pytest",
            "Alta"
        )
    else:
        logar(f"✅ Encontrados {len(test_files)} arquivos de teste")
        # Simulação de Pytest
        for test_file in test_files:
            try:
                with open(test_file, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                if "assert" not in conteudo:
                    registrar_erro(
                        "Testes",
                        f"Teste sem asserções em {test_file}",
                        "Teste não verifica comportamento",
                        "Testes ineficazes",
                        "Adicionar asserções nos testes",
                        "Média"
                    )
                else:
                    logar(f"✅ {test_file} contém asserções")
            except Exception as e:
                registrar_erro(
                    "Testes",
                    f"Erro ao analisar {test_file}",
                    f"Falha na leitura: {e}",
                    "Impossível verificar testes",
                    "Verificar formato do arquivo",
                    "Média"
                )

def verificar_documentacao() -> None:
    """Verifica a presença e qualidade da documentação."""
    logar("\n📚 Verificando documentação...")
    readme_path = PROJETO / "README.md"
    if not readme_path.exists():
        registrar_erro(
            "Documentação",
            "README.md ausente",
            "Falta de documentação inicial",
            "Dificulta uso e instalação",
            "Criar README.md com instruções",
            "Média"
        )
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            conteudo = f.read()
            if len(conteudo) < 100:
                registrar_erro(
                    "Documentação",
                    "README.md incompleto",
                    "Conteúdo insuficiente",
                    "Dificulta entendimento do projeto",
                    "Adicionar seções de instalação, uso e exemplos",
                    "Média"
                )
            else:
                logar(f"✅ README.md presente e parece completo")

def verificar_manutencao() -> None:
    """Verifica a facilidade de manutenção e extensibilidade."""
    logar("\n🔧 Verificando manutenção...")
    git_path = PROJETO / ".git"
    if not git_path.exists():
        registrar_erro(
            "Manutenção",
            "Repositório Git ausente",
            "Falta de controle de versão",
            "Dificulta colaboração e rastreamento",
            "Inicializar repositório com 'git init'",
            "Média"
        )
    else:
        logar(f"✅ Repositório Git presente")

def verificar_conformidade(regulamentos: Dict) -> None:
    """Verifica conformidade com regulamentações."""
    logar("\n📜 Verificando conformidade...")
    if regulamentos.get("regulamentacao") == "GDPR":
        for path in (PROJETO / "src").rglob("*"):
            if path.suffix in [".py", ".js"]:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        conteudo = f.read()
                    if "consent" not in conteudo.lower():
                        registrar_erro(
                            "Conformidade",
                            "Falta de consentimento do usuário",
                            "Não conformidade com GDPR",
                            "Risco legal",
                            "Adicionar tela de consentimento",
                            "Alta"
                        )
                    else:
                        logar(f"✅ Consentimento parece implementado em {path}")
                except Exception as e:
                    registrar_erro(
                        "Conformidade",
                        f"Erro ao analisar {path}",
                        f"Falha na leitura: {e}",
                        "Impossível verificar conformidade",
                        "Verificar formato do arquivo",
                        "Média"
                    )

def verificar_desempenho() -> None:
    """Verifica desempenho e escalabilidade."""
    logar("\n⚡ Verificando desempenho...")
    for path in (PROJETO / "src").rglob("*"):
        if path.suffix in [".py", ".sql"]:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                if "SELECT" in conteudo and "INDEX" not in conteudo:
                    registrar_erro(
                        "Desempenho",
                        f"Consulta SQL sem índice em {path}",
                        "Falta de otimização",
                        "Latência em grandes volumes de dados",
                        "Adicionar índices nas colunas usadas em WHERE",
                        "Média"
                    )
                else:
                    logar(f"✅ {path} parece otimizado")
            except Exception as e:
                registrar_erro(
                    "Desempenho",
                    f"Erro ao analisar {path}",
                    f"Falha na leitura: {e}",
                    "Impossível verificar desempenho",
                    "Verificar formato do arquivo",
                    "Média"
                )

def verificar_integracoes() -> None:
    """Verifica integrações com sistemas externos."""
    logar("\n🔗 Verificando integrações...")
    for path in (PROJETO / "src").rglob("*"):
        if path.suffix in [".py", ".js"]:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                if "requests.get" in conteudo and "try" not in conteudo:
                    registrar_erro(
                        "Integrações",
                        f"Chamada de API sem tratamento de erros em {path}",
                        "Falta de tolerância a falhas",
                        "Falha se a API estiver offline",
                        "Adicionar try/except com fallback",
                        "Alta"
                    )
                else:
                    logar(f"✅ {path} parece tratar erros de API")
            except Exception as e:
                registrar_erro(
                    "Integrações",
                    f"Erro ao analisar {path}",
                    f"Falha na leitura: {e}",
                    "Impossível verificar integrações",
                    "Verificar formato do arquivo",
                    "Média"
                )

def verificar_renderizacao() -> None:
    """Verifica se imagens podem ser abertas com PIL."""
    logar("\n🖼️ Verificando renderização de imagens...")
    for path in PROJETO.rglob("*.[jpg|png]"):
        try:
            with Image.open(path) as img:
                img.verify()
            logar(f"✅ {path} aberta com sucesso")
        except Exception as e:
            registrar_erro(
                "Renderização",
                f"Erro ao abrir {path}",
                f"Imagem inválida: {e}",
                "Imagens não podem ser usadas",
                "Substituir ou corrigir imagem",
                "Média"
            )

def salvar_relatorio() -> None:
    """Salva o relatório de diagnóstico."""
    severidades = {"Baixa": 1, "Média": 2, "Alta": 3}
    severidade_max = max((severidades[e["severidade"]] for e in erros), default=1) if erros else 1
    status = "Aprovado" if not erros else "Precisa de Correções"

    relatorio = [
        f"🧠 Relatório de Diagnóstico Supremo Final 11.1",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Caminho do Projeto: {PROJETO}",
        "",
        "### Resumo",
        f"- Total de erros encontrados: {len(erros)}",
        f"- Severidade: {'Baixa' if severidade_max == 1 else 'Média' if severidade_max == 2 else 'Alta'}",
        f"- Status: {status}",
        "",
        "### Detalhes por Categoria"
    ]

    categorias = sorted(set(e["categoria"] for e in erros))
    for categoria in categorias:
        relatorio.append(f"#### {categoria}")
        for erro in [e for e in erros if e["categoria"] == categoria]:
            relatorio.extend([
                f"- Erro: {erro['erro']}",
                f"- Causa: {erro['causa']}",
                f"- Impacto: {erro['impacto']}",
                f"- Correção: {erro['correcao']}",
                f"- Severidade: {erro['severidade']}",
                ""
            ])

    relatorio.extend([
        "### Recomendações Gerais",
        "- Revisar todos os erros listados e aplicar correções",
        "- Rodar novo diagnóstico após correções",
        "",
        "### Próximos Passos",
        "- Aprovar este relatório ou apontar erros adicionais",
        "- Corrigir os erros e executar novamente o diagnóstico",
        "",
        f"📁 Relatório salvo em: {ARQUIVO_RELATORIO.absolute()}"
    ])

    relatorio.extend(log)  # Inclui logs detalhados
    with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as f:
        f.write("\n".join(relatorio))
    logar(f"📁 Relatório salvo em: {ARQUIVO_RELATORIO.absolute()}")

def main(requisitos: List[str] = None, regulamentos: Dict = None) -> None:
    """Executa o diagnóstico completo."""
    logar("🚀 Iniciando Diagnóstico Supremo Final 11.1...\n")
    requisitos = requisitos or ["criar", "editar", "excluir"]  # Padrão para exemplo
    regulamentos = regulamentos or {}

    verificar_estrutura_basica()
    verificar_funcionalidades(requisitos)
    verificar_codigo()
    verificar_seguranca()
    verificar_usabilidade()
    verificar_testes()
    verificar_documentacao()
    verificar_manutencao()
    verificar_conformidade(regulamentos)
    verificar_desempenho()
    verificar_integracoes()
    verificar_renderizacao()
    salvar_relatorio()
    logar("✅ Diagnóstico finalizado com sucesso.")

if __name__ == "__main__":
    # Exemplo de requisitos para teste
    main(
        requisitos=["criar_tarefa", "editar_tarefa", "excluir_tarefa"],
        regulamentos={"regulamentacao": "GDPR"}
    )
