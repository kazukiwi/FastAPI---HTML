#pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="API de Alunos")

#Rodar o servidor
#python -m uvicorn main:app --reload

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
    },
    {
        "nome": "Kazuki",
        "nota": 5.5
    },
    {
        "nome": "Vitória",
        "nota": 4.5
    }
]

#Rota inicial
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "alunos.html", {"request": request, "listar_alunos": alunos}
    )

#Rota de cadastro (Tela cadastro)
@app.get("/cadastro", response_class=HTMLResponse)
def cadastro(request: Request):
    return templates.TemplateResponse(
        "cadastro.html", {"request": request}
    )

#Rota de cadastro na lista
@app.post("/cadastro")
def salvar_aluno(nome: str = Form(...), nota: float = Form(...)):
    alunos.append({"nome": nome, "nota": nota})
    return RedirectResponse(url="/", status_code=303)