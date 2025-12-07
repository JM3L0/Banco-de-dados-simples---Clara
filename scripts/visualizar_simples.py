import sqlite3
import os

# Obter o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Caminho do banco de dados
db_path = os.path.join(script_dir, '..', 'database', 'remume_2025.db')

# Conectar ao banco
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Mostrar todos os medicamentos de forma simples
cursor.execute('SELECT * FROM medicamentos ORDER BY denominacao_comum')
medicamentos = cursor.fetchall()

print(f"\n{'ID':<5} {'MEDICAMENTO':<50} {'CONCENTRAÇÃO':<25} {'FORMA':<30}")
print("="*120)

for med in medicamentos:
    id_med = str(med[0])
    nome = med[1][:48] if med[1] else ""
    conc = med[2][:23] if med[2] else ""
    forma = med[3][:28] if med[3] else ""
    print(f"{id_med:<5} {nome:<50} {conc:<25} {forma:<30}")

print(f"\nTotal: {len(medicamentos)} medicamentos")

conn.close()
