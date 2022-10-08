from fastapi import FastAPI
app = FastAPI()
#Criando a conexão com o Oracle
import cx_Oracle
# ajustar para a pasta onde descompactou o client do oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_6") #deixar o caminho conforme recomendado ao lado e verificar se a versão do seu instantclient

#con = cx_Oracle.connect("user/senha@conexão/xe") #Estabelcendo conexão com o banco de dados cx_Oracle

print("Conexão estabelecida com Oracle versão "+con.version) #sucess

# ----------------------------------------------------
# para carregar os arquivos estáticos da parte web
# Ficarão acessíveis por http://localhost:8000/web/
#from fastapi.staticfiles import StaticFiles
#app.mount("/projeto", StaticFiles(
    #directory="./projeto", html="index.js"), name="Index")
# ----------------------------------------------------


# GET quando o cliente vai obter dados do servidor
@app.get("/")
def boas_vindas():
  return {"mensagem": "Bem vindo ao servido da API! Acesse http://localhost:8000/docs"} 

import login #Importação da rota de login
app.include_router(login.router)



