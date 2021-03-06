from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel

from config.settings import ALLOWED_HOSTS
from utils.vowels import reverse_vowels
from database import models
from database.database import engine

from routes import todo

# create tables
models.Base.metadata.create_all(bind=engine)


class VowelPayload(BaseModel):
    message: str


app = FastAPI()

app.include_router(todo.router, prefix='/todo')


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=ALLOWED_HOSTS)


@app.get("/hello")
async def hello():
    return "world"


@app.post("/vowel-service")
async def vowel_service(payload: VowelPayload):
    message = payload.message
    message_reversed_vowels = reverse_vowels(message)
    return message_reversed_vowels


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
