from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from fastapi import APIRouter, HTTPException

import cx_Oracle
#con = cx_Oracle.connect("user/senha@conexão/xe") #Estabelcendo conexão com o banco de dados cx_Oracle

router = APIRouter()

class Usuario(BaseModel):
    codigoUsuario: Optional[int]
    nome: str
    senha: str

### LISTANDO USUARIO ###
@router.get("/Usuario")
def listar():
    try:
        cursor = con.cursor()
        rows = cursor.execute(
            "SELECT * FROM tabelaUsuario"
            ).fetchall()
        cursor.close()
        lista = []
        for r in rows:
            dic = {
                "Usuario": r[0],
                "nome": r[1],
                "senha": r[2]
            }
            lista.append(dic)
        return lista
    except Exception as ex:
        raise HTTPException(status_code=400, detail=format(ex))



### INSERINDO USUARIO ###
@router.post("/Usuario")
def inserir(obj: Usuario):
    try:
        cursor = con.cursor()
        sql = "INSERT INTO Usuario "
        sql += "(Usuario, nome, senha)"
        sql += " VALUES "
        sql += "(SQ_Usuario.nextval, :nome, :senha)"
        cursor.execute(sql, {
            "nome": obj.nome,
            "senha": obj.senha
        })
        cursor.close()
        con.commit()
        return "ok";
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=400, detail=format(ex))



### ALTERANDO USUARIO ###
@router.put("/Usuario")
def alterar(obj: Usuario):
    try:
        cursor = con.cursor()
        sql = "UPDATE Usuario "
        sql += "SET nome = :nome, senha = :senha"
        sql += " WHERE "
        sql += "Usuario = :Usuario "
        cursor.execute(sql, {
            "nome": obj.nome,
            "codigoUsuario": obj.codigoUsuario,
            "senha": obj.senha
        })
        cursor.close()
        con.commit()
        return "ok";
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=400, detail=format(ex))


### EXCLUINDO USUARIO (PASSAR O USUARIO POR PARAMETRO)###
@router.delete("/Usuario/{Usuario}")
def excluir(codigoUsuario: int):
    try:
        cursor = con.cursor()
        sql = "DELETE FROM Usuario "
        sql += " WHERE "
        sql += "Usuario = :Usuario "
        cursor.execute(sql, {
            "Usuario": Usuario
        })
        cursor.close()
        con.commit()
        return "ok";
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=400, detail=format(ex))
