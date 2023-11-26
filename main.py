### Hola Mundo ###

# Documentación oficial: https://dastapi.tiangolo.com/es/

# Instala FastApi: pip install "fastapi[all]"

from fastapi import FastAPI

app = FastAPI()


# Url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "¡Hola FastApi!"


# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}

# Inicia el server: unicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger http://127.0.0.1:8000/docs
# Documentación con Redocly http://127.0.0.1:8000/redocs
