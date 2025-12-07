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

print(f"\n{'ID':<5} {'MEDICAMENTO':<35} {'CONCENTRAÇÃO':<20} {'FORMA':<25} {'ESPECIFICAÇÃO':<20} {'UNIDADE':<15}")
print("="*130)

for med in medicamentos:
    id_med = str(med[0])
    nome = med[1][:33] if med[1] else ""
    conc = med[2][:18] if med[2] else ""
    forma = med[3][:23] if med[3] else ""
    espec = med[4][:18] if med[4] else ""
    unid = med[5][:13] if med[5] else ""
    print(f"{id_med:<5} {nome:<35} {conc:<20} {forma:<25} {espec:<20} {unid:<15}")

print(f"\nTotal: {len(medicamentos)} medicamentos")

conn.close()
