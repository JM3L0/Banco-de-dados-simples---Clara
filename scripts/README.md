# Scripts do Banco de Dados REMUME 2025

Este diretório contém todos os scripts Python para gerenciar e consultar o banco de dados.

## 📄 Scripts Disponíveis

### `criar_banco_remume.py`
Extrai dados do PDF e cria o banco de dados SQLite.

**Como usar:**
```bash
python criar_banco_remume.py
```

**O que faz:**
- Lê o arquivo PDF "REMUME 2025 (1).pdf"
- Extrai tabelas com medicamentos
- Cria o banco de dados em `../database/remume_2025.db`
- Insere 246 medicamentos

---

### `consultar_remume.py`
Sistema interativo com menu de opções.

**Como usar:**
```bash
python consultar_remume.py
```

**Funcionalidades:**
- Listar todos os medicamentos
- Buscar por nome (busca parcial)
- Buscar por forma farmacêutica
- Exibir estatísticas completas

---

### `verificar_banco.py`
Verifica integridade e mostra estatísticas detalhadas.

**Como usar:**
```bash
python verificar_banco.py
```

**Exibe:**
- Total de medicamentos
- Distribuição por forma farmacêutica
- Exemplos de buscas

---

### `visualizar_simples.py`
Exibe todos os medicamentos em formato de tabela.

**Como usar:**
```bash
python visualizar_simples.py
```

**Saída:**
- Tabela formatada com todos os medicamentos
- Ordenados alfabeticamente

---

### `extrair_pdf.py`
Análise exploratória do PDF (usado durante desenvolvimento).

**Como usar:**
```bash
python extrair_pdf.py
```

## 💡 Dicas

Todos os scripts devem ser executados a partir deste diretório `scripts/` para que os caminhos relativos funcionem corretamente.

Se executar de outro local, ajuste os caminhos no código.
