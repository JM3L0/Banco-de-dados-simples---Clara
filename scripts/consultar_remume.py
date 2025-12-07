import sqlite3
import sys
import os

def conectar_banco():
    """Conecta ao banco de dados REMUME 2025"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, '..', 'database', 'remume_2025.db')
    return sqlite3.connect(db_path)

def listar_todos():
    """Lista todos os medicamentos"""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM medicamentos ORDER BY denominacao_comum')
    medicamentos = cursor.fetchall()
    
    print(f"\n{'='*100}")
    print(f"TOTAL DE MEDICAMENTOS: {len(medicamentos)}")
    print(f"{'='*100}\n")
    
    for med in medicamentos:
        print(f"ID: {med[0]} | {med[1]} - {med[2]} - {med[3]}")
    
    conn.close()

def buscar_por_nome(nome):
    """Busca medicamentos por nome (parcial)"""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM medicamentos 
        WHERE denominacao_comum LIKE ? 
        ORDER BY denominacao_comum
    ''', (f'%{nome}%',))
    
    resultados = cursor.fetchall()
    
    if resultados:
        print(f"\n{'='*100}")
        print(f"ENCONTRADOS {len(resultados)} RESULTADO(S) PARA: '{nome}'")
        print(f"{'='*100}\n")
        
        for med in resultados:
            print(f"ID: {med[0]}")
            print(f"Nome: {med[1]}")
            print(f"Concentração: {med[2]}")
            print(f"Forma Farmacêutica: {med[3]}")
            print(f"Página no PDF: {med[4]}")
            print("-" * 100)
    else:
        print(f"\nNenhum medicamento encontrado com o nome '{nome}'")
    
    conn.close()

def buscar_por_forma(forma):
    """Busca medicamentos por forma farmacêutica"""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM medicamentos 
        WHERE forma_farmaceutica LIKE ? 
        ORDER BY denominacao_comum
    ''', (f'%{forma}%',))
    
    resultados = cursor.fetchall()
    
    if resultados:
        print(f"\n{'='*100}")
        print(f"ENCONTRADOS {len(resultados)} MEDICAMENTO(S) NA FORMA: '{forma}'")
        print(f"{'='*100}\n")
        
        for med in resultados:
            print(f"{med[1]} - {med[2]}")
    else:
        print(f"\nNenhum medicamento encontrado na forma '{forma}'")
    
    conn.close()

def estatisticas():
    """Mostra estatísticas do banco de dados"""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    # Total de medicamentos
    cursor.execute('SELECT COUNT(*) FROM medicamentos')
    total = cursor.fetchone()[0]
    
    # Formas farmacêuticas distintas
    cursor.execute('SELECT DISTINCT forma_farmaceutica FROM medicamentos WHERE forma_farmaceutica IS NOT NULL')
    formas = cursor.fetchall()
    
    # Top 10 formas mais comuns
    cursor.execute('''
        SELECT forma_farmaceutica, COUNT(*) as qtd 
        FROM medicamentos 
        WHERE forma_farmaceutica IS NOT NULL 
        GROUP BY forma_farmaceutica 
        ORDER BY qtd DESC 
        LIMIT 10
    ''')
    top_formas = cursor.fetchall()
    
    print(f"\n{'='*100}")
    print("ESTATÍSTICAS DO BANCO DE DADOS REMUME 2025")
    print(f"{'='*100}\n")
    print(f"Total de medicamentos cadastrados: {total}")
    print(f"Total de formas farmacêuticas distintas: {len(formas)}\n")
    print("Top 10 formas farmacêuticas mais comuns:")
    print("-" * 100)
    for forma, qtd in top_formas:
        print(f"{forma}: {qtd} medicamento(s)")
    
    conn.close()

def menu():
    """Exibe menu de opções"""
    print("\n" + "="*100)
    print("SISTEMA DE CONSULTA - REMUME 2025")
    print("="*100)
    print("1 - Listar todos os medicamentos")
    print("2 - Buscar medicamento por nome")
    print("3 - Buscar por forma farmacêutica")
    print("4 - Exibir estatísticas")
    print("0 - Sair")
    print("="*100)

def main():
    """Função principal"""
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            listar_todos()
        elif opcao == '2':
            nome = input("Digite o nome do medicamento (ou parte dele): ").strip()
            if nome:
                buscar_por_nome(nome)
        elif opcao == '3':
            forma = input("Digite a forma farmacêutica: ").strip()
            if forma:
                buscar_por_forma(forma)
        elif opcao == '4':
            estatisticas()
        elif opcao == '0':
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
