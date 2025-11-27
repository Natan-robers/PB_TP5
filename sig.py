from data.conexao import inicializar_banco, fechar_sessao, obter_sessao
from data.modelos import Base
from services.sig.servico_excel import carregar_dados_excel
from views.sig.menu_principal import menu_principal_sig

def principal():
    try:
        inicializar_banco(Base)
        print("SIG - Sistema de Informações Gerenciais")
        print("=" * 50)
        
        obter_sessao()
        
        carregar_dados_excel()
        
        menu_principal_sig()
    finally:
        fechar_sessao()

if __name__ == '__main__':
    principal()
