# Banco de Dados REMUME 2025

Banco de dados SQLite com 246 medicamentos extraídos do PDF REMUME 2025.

## Estrutura

```
├── database/remume_2025.db     # Banco de dados
├── scripts/                     # Scripts Python
└── REMUME 2025 (1).pdf         # PDF original
```

## Como Usar

```bash
# Visualizar todos os medicamentos
python scripts/visualizar_simples.py

# Sistema de consulta interativo
python scripts/consultar_remume.py

# Verificar dados do Banco de Dados 
python scripts/verificar_banco.py

## Tabela: medicamentos

- `id` - Identificador
- `denominacao_comum` - Nome do medicamento
- `concentracao` - Concentração
- `forma_farmaceutica` - Comprimido, cápsula, etc.
- `especificacao` - Público-alvo (criança, adulto, obesos, etc.)
- `unidade` - Forma de contagem (caixa, unidade única, etc.)
