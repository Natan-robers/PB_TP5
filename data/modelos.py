from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Integer, default=0)
    preco = Column(Float, default=0.0)

    def __repr__(self):
        return f"<Produto id={self.id} nome='{self.nome}' qtd={self.quantidade} preco={self.preco}>"

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    def __repr__(self):
        return f"<Cliente id={self.id} nome='{self.nome}'>"


  
