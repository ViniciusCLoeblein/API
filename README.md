# API
Repositorio de API examples em python

#Dependecias
#fastapi==0.78.0
#uvicorn==0.17.6
#pydantic==1.9.1
#aiofiles==0.7.0
#cx-Oracle



# --------------------------------------------------------
# PARA CRIAR O AMBIENTE EM UMA MÁQUINA DO ZERO
# --------------------------------------------------------
# Para criar a VM para nosso projeto (venv)
# Somente no início para criar o ambiente virtual
python -m venv venv

# Para ativar o ambiente virtual (venv) verdinho no canto esquerdo do terminal.
# É preciso ativar sempre antes de rodar a API
venv\Scripts\activate 

# Para dar permissão no VSCode - só na primeira vez se o comando acima não funcionar
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

# Para Rodar o servidor da API
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Para testar a API
http://localhost:8000/docs

# certificar-se de que o cliente do oracle está correto

# para o emulador acessar a api / com o emulador já aberto 
adb reverse tcp:8000 tcp:8000
