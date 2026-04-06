from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    produtos = relationship("Produto", back_populates="fornecedores")

    
    def __repr__(self):
        return f"Fornecedor: ID = {self.id} - NOME = {self.nome}"
    
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)

   
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    
    fornecedor = relationship("Fornecedor", back_populates="produtos")

    def __repr__(self):
        return f"Produto: ID = {self.id} - NOME = {self.nome} - PREÇO = {self.preco}"
    
engine = create_engine("sqlite:///empresa.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)