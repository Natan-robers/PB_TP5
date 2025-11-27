import pandas as pd

def criar_arquivo_fornecedores():
    df_fornecedores = pd.DataFrame({
        'nome': [
            'Fornecedor A',
            'Fornecedor B',
            'Fornecedor C',
            'Fornecedor D'
        ]
    })
    
    df_produtos_fornecedores = pd.DataFrame({
        'id_produto': [1, 2, 3, 1, 4],
        'id_fornecedor': [1, 1, 2, 2, 3]
    })
    
    with pd.ExcelWriter('fornecedores.xlsx', engine='openpyxl') as writer:
        df_fornecedores.to_excel(writer, sheet_name='fornecedores', index=False)
        df_produtos_fornecedores.to_excel(writer, sheet_name='produtos-fornecedores', index=False)
    
    print("Arquivo fornecedores.xlsx criado com sucesso!")
    print("\nEstrutura criada:")
    print("- Aba 'fornecedores':", len(df_fornecedores), "fornecedores")
    print("- Aba 'produtos-fornecedores':", len(df_produtos_fornecedores), "associacoes")
    print("\nIMPORTANTE: Ajuste os IDs de produtos conforme os produtos existentes no banco!")

if __name__ == '__main__':
    criar_arquivo_fornecedores()

