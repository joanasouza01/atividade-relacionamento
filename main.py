from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(Integer, nullable=False)
    endereco = Column(String(100), nullable=False)

    produtos = relationship("Produto", back_populates="fornecedores")

    
    def __repr__(self):
        return f"Fornecedor: ID = {self.id} - NOME = {self.nome} - CPF {self.cpf} - ENDEREÇO {self.endereco}"
    
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    entrega = Column(String(100), nullable=False)

   
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    
    fornecedores = relationship("Fornecedor", back_populates="produtos")

    def __repr__(self):
        return f"Produto: ID = {self.id} - NOME = {self.nome} - PREÇO = {self.preco} - ENDEREÇO DE ENTREGA = {self.entrega}"
    
engine = create_engine("sqlite:///negocio.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

#Funções

def cadastrar_fornecedor():
    with Session() as session:
        try:
            nome_f = input("Digite o nome do fornecedor que deseja cadastrar: ").strip().capitalize()
            cpf_f = input("Digite o CPF (Registro Nacional) do fornecedor: ").capitalize()
            endereco_f = input("Digite o endereço do fornecedor: ").capitalize()

            fornecedor = Fornecedor(nome=nome_f, cpf=cpf_f, endereco=endereco_f)
            session.add(fornecedor)
            session.commit()
            print("deu certo!")

        except Exception as erro:
            session.rollback()
            print(f"deu ruim! {erro}")


def cadastrar_produto():
    with Session() as session:
        try:
            nome_p = input("Digite o nome do produto que deseja cadastrar: ").strip().capitalize()
            preco_p = input("Digite o preço do produto: ").capitalize()
            entrega_p = input("Digite o endereço de entrega do produto: ").capitalize()

            produto = Produto(nome=nome_p, preco=preco_p, entrega=entrega_p)
            session.add(produto)
            session.commit()
            print("deu certo!")

        except Exception as erro:
            session.rollback()
            print(f"deu ruim! {erro}")

# cadastrar_produto()

#consulta
def listar_fornecedor():
    with Session() as session:
        try:
            if fornecedor == None:
                print("Não encontrado")
            else:

                fornecedor = session.query(Fornecedor).all()
                for f in fornecedor:
                    print(f"\n{f}")
                    for p in f.produtos:
                        print(p.fornecedor)
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

# listar_fornecedor()

