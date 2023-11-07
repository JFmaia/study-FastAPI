from fastapi import FastAPI

## instanciando o fastAPI
app = FastAPI()

@app.get('/mensagem')
async def mensagem(): 
    return {"msg": "FastAPI na Geek University"}

# Modificação para rodar o arquivo direto pelo python
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)