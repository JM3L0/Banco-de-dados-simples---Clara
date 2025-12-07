# Banco de Dados REMUME 2025

Sistema de banco de dados SQLite com todos os medicamentos da REMUME 2025 (Relação Municipal de Medicamentos Essenciais).

## 📁 Estrutura do Projeto

```
Banco de dados simples/
│
├── database/                    # Banco de dados
│   └── remume_2025.db          # SQLite database com 246 medicamentos
│
├── scripts/                     # Scripts Python
│   ├── criar_banco_remume.py   # Cria o banco a partir do PDF
│   ├── consultar_remume.py     # Sistema interativo de consulta
│   ├── verificar_banco.py      # Verifica e exibe estatísticas
│   ├── visualizar_simples.py   # Visualização simples em tabela
│   └── extrair_pdf.py          # Análise exploratória do PDF
│
├── docs/                        # Documentação
│   └── README.md               # Documentação completa
│
└── REMUME 2025 (1).pdf         # PDF original com os dados
```

## 🚀 Como Usar

### 1. Visualizar o Banco de Dados

**Opção 1: Sistema Interativo**
```bash
cd scripts
python consultar_remume.py
```

**Opção 2: Visualização Simples**
```bash
cd scripts
python visualizar_simples.py
```

**Opção 3: VS Code SQLite Viewer**
- Clique no arquivo `database/remume_2025.db` no Explorer

### 2. Recriar o Banco de Dados

```bash
cd scripts
python criar_banco_remume.py
```

### 3. Ver Estatísticas

```bash
cd scripts
python verificar_banco.py
```

## 📊 Informações

- **Total de medicamentos**: 246
- **Páginas no PDF**: 14
- **Formas farmacêuticas**: 50+ tipos diferentes

## 🔍 Estrutura da Tabela

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | ID único |
| denominacao_comum | TEXT | Nome do medicamento |
| concentracao | TEXT | Concentração/composição |
| forma_farmaceutica | TEXT | Forma (comprimido, cápsula, etc.) |
| pagina | INTEGER | Página do PDF original |

## 💡 Exemplos de Consulta SQL

```sql
-- Buscar medicamento
SELECT * FROM medicamentos WHERE denominacao_comum LIKE '%Dipirona%';

-- Listar comprimidos
SELECT * FROM medicamentos WHERE forma_farmaceutica = 'Comprimido';

-- Contar por forma
SELECT forma_farmaceutica, COUNT(*) 
FROM medicamentos 
GROUP BY forma_farmaceutica;
```

## 📦 Requisitos

- Python 3.12+
- pdfplumber
- PyPDF2

```bash
pip install pdfplumber PyPDF2
```
