from dados.conexao import obter_sessao
from dados.modelos import Produto

def obter_produto_por_id(id_produto):
    session = obter_sessao()
    return session.query(Produto).filter(Produto.id == id_produto).first()

def salvar_ou_atualizar_produto(produto_obj):
    session = obter_sessao()
    existente = session.query(Produto).filter(Produto.id == produto_obj.id).first()
    if existente:
        existente.nome = produto_obj.nome
        existente.quantidade = produto_obj.quantidade
        existente.preco = produto_obj.preco
    else:
        session.add(produto_obj)
    session.commit()

def buscar_produtos_sem_estoque():
    session = obter_sessao()
    return session.query(Produto).filter(Produto.quantidade == 0).all()

def decrementar_estoque(id_produto, quantidade):
    session = obter_sessao()
    p = session.query(Produto).filter(Produto.id == id_produto).first()
    if p:
        p.quantidade = max(0, p.quantidade - quantidade)
    session.commit()

def listar_todos_produtos():
    session = obter_sessao()
    return session.query(Produto).order_by(Produto.id).all()

def contar_produtos():
    session = obter_sessao()
    return session.query(Produto).count()
