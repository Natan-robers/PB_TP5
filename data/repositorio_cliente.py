from data.conexao import obter_sessao
from data.modelos import Cliente

def obter_cliente_por_id(id_cliente):
    session = obter_sessao()
    return session.query(Cliente).filter(Cliente.id == id_cliente).first()

def buscar_cliente_por_nome(nome):
    session = obter_sessao()
    return session.query(Cliente).filter(Cliente.nome == nome).first()

def salvar_cliente(nome=None):
    session = obter_sessao()
    c = Cliente(nome=nome or "Cliente")
    session.add(c)
    session.flush()          # Força geração do ID no SQLite
    session.refresh(c)       # Atualiza o objeto com o ID
    # Se nome não foi fornecido ou é "Cliente", atualiza com o ID gerado
    if nome is None or nome == "Cliente":
        c.nome = f"Cliente {c.id}"
    session.commit()         # Commit após salvar
    return c.id              # ✅ return é SOMENTE o número
