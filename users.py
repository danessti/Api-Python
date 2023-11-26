from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int


users_list = (([User(name="Brais", surname="moure", url="https://moure.dev", age=35),
         User(name="Moure", surname="Dev", url="https://mouredev.com", age=35),
         User(name="Haakom", surname="Dahberg", url="https://haakon.com", age=33)]))


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surnemae": "moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surnemae": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakom", "surnemae": "Dahberg", "url": "https://haakon.com", "age": 33}]


@app.get("/users")
async def users():
    return users_list