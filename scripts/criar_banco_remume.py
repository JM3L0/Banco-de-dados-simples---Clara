import sqlite3
import pdfplumber
import re
import os

# Obter o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho do PDF
pdf_path = os.path.join(script_dir, '..', 'REMUME 2025 (1).pdf')

# Caminho do banco de dados
db_path = os.path.join(script_dir, '..', 'database', 'remume_2025.db')

# Criar conexão com o banco de dados
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criar tabela de medicamentos
cursor.execute('''
CREATE TABLE IF NOT EXISTS medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    denominacao_comum TEXT NOT NULL,
    concentracao TEXT,
    forma_farmaceutica TEXT,
    pagina INTEGER
)
''')

print("Banco de dados criado com sucesso!")
print("Extraindo dados do PDF...\n")

# Extrair dados do PDF
medicamentos = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        # Extrair tabelas da página
        tables = page.extract_tables()
        
        for table in tables:
            # Ignorar cabeçalho (primeira linha)
            for row in table[1:]:
                if row and len(row) >= 3:
                    denominacao = row[0]
                    concentracao = row[1]
                    forma_farmaceutica = row[2]
                    
                    # Limpar quebras de linha nos dados
                    if denominacao:
                        denominacao = denominacao.replace('\n', ' ').strip()
                    if concentracao:
                        concentracao = concentracao.replace('\n', ' ').strip()
                    if forma_farmaceutica:
                        forma_farmaceutica = forma_farmaceutica.replace('\n', ' ').strip()
                    
                    # Verificar se há dados válidos
                    if denominacao and denominacao != '':
                        medicamentos.append((
                            denominacao,
                            concentracao if concentracao else None,
                            forma_farmaceutica if forma_farmaceutica else None,
                            page_num
                        ))

# Inserir dados no banco
cursor.executemany('''
    INSERT INTO medicamentos (denominacao_comum, concentracao, forma_farmaceutica, pagina)
    VALUES (?, ?, ?, ?)
''', medicamentos)

conn.commit()

# Mostrar estatísticas
cursor.execute('SELECT COUNT(*) FROM medicamentos')
total = cursor.fetchone()[0]
print(f"Total de medicamentos inseridos: {total}\n")

# Mostrar alguns exemplos
print("Primeiros 10 medicamentos cadastrados:")
print("-" * 80)
cursor.execute('SELECT * FROM medicamentos LIMIT 10')
for row in cursor.fetchall():
    print(f"ID: {row[0]}")
    print(f"Nome: {row[1]}")
    print(f"Concentração: {row[2]}")
    print(f"Forma Farmacêutica: {row[3]}")
    print(f"Página: {row[4]}")
    print("-" * 80)

conn.close()
print("\nBanco de dados 'remume_2025.db' criado com sucesso!")
