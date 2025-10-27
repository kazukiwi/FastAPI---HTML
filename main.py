#pip install fastapi uvicorn jinja2
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI("API de Alunos")

#Configura o diretório dos templates jinja2
templates = Jinja2Templates(directory="templates")

#Pasta static para servir os arquivos (CSS, Imagens ou JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

alunos = [
    {
        "nome": "Kazuki",
        "nota": 10.0
    },
    {
        "nome": "Laura",
        "nota": 10.0
    },
    {
        "nome": "Joanna",
        "nota": 7.5
    }
]

#Rota inicial
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "alunos.html", {"request": request, "listar_alunos": alunos}
    )
