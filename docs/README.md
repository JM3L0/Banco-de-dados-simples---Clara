# Banco de Dados REMUME 2025

Este projeto contém um banco de dados SQLite com todos os medicamentos da REMUME 2025 (Relação Municipal de Medicamentos Essenciais).

## Arquivos

- `remume_2025.db` - Banco de dados SQLite com os medicamentos
- `criar_banco_remume.py` - Script para criar o banco de dados a partir do PDF
- `consultar_remume.py` - Sistema interativo de consulta
- `extrair_pdf.py` - Script auxiliar para análise do PDF

## Estrutura do Banco de Dados

### Tabela: medicamentos

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Identificador único (chave primária) |
| denominacao_comum | TEXT | Nome do medicamento (DCB - Denominação Comum Brasileira) |
| concentracao | TEXT | Concentração ou composição |
| forma_farmaceutica | TEXT | Forma farmacêutica (comprimido, cápsula, etc.) |
| pagina | INTEGER | Página do PDF original |

## Como Usar

### 1. Criar o Banco de Dados

```bash
python criar_banco_remume.py
```

Este comando irá:
- Ler o arquivo PDF "REMUME 2025 (1).pdf"
- Extrair todos os medicamentos
- Criar o banco de dados SQLite com 246 medicamentos

### 2. Consultar o Banco de Dados

#### Modo Interativo

```bash
python consultar_remume.py
```

Menu de opções:
- **1** - Listar todos os medicamentos
- **2** - Buscar medicamento por nome
- **3** - Buscar por forma farmacêutica
- **4** - Exibir estatísticas
- **0** - Sair

#### Consultas SQL Diretas

Você também pode usar qualquer cliente SQLite para consultar o banco:

```sql
-- Buscar um medicamento específico
SELECT * FROM medicamentos WHERE denominacao_comum LIKE '%Amoxicilina%';

-- Listar todos os comprimidos
SELECT * FROM medicamentos WHERE forma_farmaceutica LIKE '%Comprimido%';

-- Contar medicamentos por forma farmacêutica
SELECT forma_farmaceutica, COUNT(*) as total 
FROM medicamentos 
GROUP BY forma_farmaceutica 
ORDER BY total DESC;
```

### 3. Exemplos de Uso Python

```python
import sqlite3

# Conectar ao banco
conn = sqlite3.connect('remume_2025.db')
cursor = conn.cursor()

# Buscar medicamento
cursor.execute("SELECT * FROM medicamentos WHERE denominacao_comum LIKE ?", ('%Dipirona%',))
resultado = cursor.fetchall()

for med in resultado:
    print(f"Nome: {med[1]}, Concentração: {med[2]}, Forma: {med[3]}")

conn.close()
```

## Estatísticas

- **Total de medicamentos**: 246
- **Páginas do PDF**: 14
- **Formas farmacêuticas**: Comprimidos, Cápsulas, Suspensões, Soluções, Cremes, etc.

## Requisitos

- Python 3.12+
- pdfplumber
- PyPDF2
- sqlite3 (já incluído no Python)

## Instalação de Dependências

```bash
pip install pdfplumber PyPDF2
```

## Autor

Sistema criado automaticamente a partir do PDF REMUME 2025.

## Data

Dezembro de 2025
