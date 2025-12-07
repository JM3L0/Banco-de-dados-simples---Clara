import pdfplumber
import json

pdf_path = r"c:\Users\jsous\OneDrive\Área de Trabalho\Banco de dados simples\REMUME 2025 (1).pdf"

with pdfplumber.open(pdf_path) as pdf:
    print(f"Total de páginas: {len(pdf.pages)}\n")
    
    # Extrair texto das primeiras páginas para análise
    for i in range(min(3, len(pdf.pages))):
        page = pdf.pages[i]
        text = page.extract_text()
        print(f"=== PÁGINA {i+1} ===")
        print(text[:2000])  # Primeiros 2000 caracteres
        print("\n" + "="*50 + "\n")
        
        # Tentar extrair tabelas
        tables = page.extract_tables()
        if tables:
            print(f"Tabelas encontradas na página {i+1}: {len(tables)}")
            for idx, table in enumerate(tables[:2]):  # Mostrar primeiras 2 tabelas
                print(f"\nTabela {idx+1}:")
                for row in table[:5]:  # Primeiras 5 linhas
                    print(row)
            print("\n")
