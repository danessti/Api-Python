### Hola Mundo ###

# Documentación oficial: https://dastapi.tiangolo.com/es/

# Instala FastApi: pip install "fastapi[all]"

from fastapi import FastAPI
import routers
from fastapi.staticfiles import StaticFiles

app: FastAPI = FastAPI()

# Routers
app.include_router(routers.products.router)
app.include_router(routers.users.router)

app.include_router(routers.basic_auth_users.router)
app.include_router(routers.jwt_auth_users.router)
app.include_router(routers.users_db.router)

# Recursos estáticos
app.mount("/statics", StaticFiles(directory="static"), name="static")


# Url local: http://127.0.0.1:8000


@app.get("/")
async def root():
    return "¡Hola FastApi!"


# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger http://127.0.0.1:8000/docs
# Documentación con Redocly http://127.0.0.1:8000/redocs

# cd se entra al archivo FastApi para ejecutar el main
