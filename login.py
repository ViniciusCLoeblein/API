from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from fastapi import APIRouter, HTTPException
import cx_Oracle

#con = cx_Oracle.connect("user/senha@conexão/xe") #Estabelcendo conexão com o banco de dados cx_Oracle

router = APIRouter()

#Definir a estrutura (classe BaseModel) para as credenciais (login e senha)
class Credenciais(BaseModel):
    codigoUsuario: int
    senha: str

#Implementar a rota e a função de autenticação que recebe as credenciais
@router.post("/autenticar") # post recebe dados - pode inserir, usar numa consulta
def autenticar(obj: Credenciais):
    try:
        cursor = con.cursor() # para poder enviar SQL para o banco
        # Fazer um select na tabela de usuários do banco de dados para verificar se encontra um usuário com o
        # código e senha recebido pelas credenciais.
        rows = cursor.execute(
            "SELECT codigoUsuario, nome FROM Usuario "+
            " WHERE codigoUsuario = :codigoUsuario "+
            "   AND senha = :senha",
            {"codigoUsuario":obj.codigoUsuario,
             "senha":obj.senha}
        ).fetchall()
        cursor.close()
        #Se a resposta do SQL resultar em uma linha (row) retornar um JSON com chave/valor para
        #codigousuario" e "nome" do usuário encontrado. 
        for r in rows:
            dic = {
                "codigoUsuario": r[0],
                "nome": r[1]
            }
            return dic;
        #Se o SQL não retornar nenhuma linha, retornar o JSON {"invalido":True}
        return {"invalido":True}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=format(ex))
