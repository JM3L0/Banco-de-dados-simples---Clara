import sqlite3
import os

# Obter o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, '..', 'database', 'remume_2025.db')

# Conectar ao banco de dados
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("="*100)
print("VERIFICAÇÃO DO BANCO DE DADOS REMUME 2025")
print("="*100)

# Verificar total de registros
cursor.execute('SELECT COUNT(*) FROM medicamentos')
total = cursor.fetchone()[0]
print(f"\nTotal de medicamentos cadastrados: {total}")

# Estatísticas por forma farmacêutica
print("\n" + "-"*100)
print("DISTRIBUIÇÃO POR FORMA FARMACÊUTICA:")
print("-"*100)
cursor.execute('''
    SELECT forma_farmaceutica, COUNT(*) as qtd 
    FROM medicamentos 
    WHERE forma_farmaceutica IS NOT NULL 
    GROUP BY forma_farmaceutica 
    ORDER BY qtd DESC
''')

for forma, qtd in cursor.fetchall():
    print(f"{forma:.<60} {qtd:>3} medicamento(s)")

# Exemplo de busca
print("\n" + "-"*100)
print("EXEMPLO: Buscando medicamentos com 'Dipirona'")
print("-"*100)
cursor.execute("SELECT * FROM medicamentos WHERE denominacao_comum LIKE '%Dipirona%'")
resultados = cursor.fetchall()

if resultados:
    for med in resultados:
        print(f"\nID: {med[0]}")
        print(f"Nome: {med[1]}")
        print(f"Concentração: {med[2]}")
        print(f"Forma: {med[3]}")
        print(f"Página: {med[4]}")
else:
    print("Nenhum resultado encontrado")

# Exemplo de busca 2
print("\n" + "-"*100)
print("EXEMPLO: Todos os medicamentos em forma de Xarope")
print("-"*100)
cursor.execute("SELECT * FROM medicamentos WHERE forma_farmaceutica LIKE '%Xarope%'")
resultados = cursor.fetchall()

for med in resultados:
    print(f"- {med[1]} ({med[2]})")

print("\n" + "="*100)
print("VERIFICAÇÃO CONCLUÍDA!")
print("="*100)

conn.close()
