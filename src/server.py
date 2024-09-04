from fastapi import FastAPI, Depends
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db, criar_db

criar_db() #Criar banco de dados

app = FastAPI()

#Para rodar a aplicação:
# uvicorn src.server:app --reload --reload-dir=src

@app.get('/')
def home():
    return {'Msg: ' 'API Funcionando'}

@app.post('/produtos')
def criar_produtos(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    lista_produto = RepositorioProduto(db).listar()
    return lista_produto

