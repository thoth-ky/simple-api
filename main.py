from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.middleware.trustedhost import TrustedHostMiddleware

from config.settings import ALLOWED_HOSTS


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=ALLOWED_HOSTS)


@app.get("/hello")
async def hello():
    return "world"


@app.post("/vowel-service", status_code=status.HTTP_201_CREATED)
async def vowel_service():
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
