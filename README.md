# Projeto: FastAPI - HTML

Pequeno projeto exemplo que serve páginas HTML com FastAPI e Jinja2.

## Pré-requisitos
- Python 3.8+
- Instalar dependências:
```sh
pip install fastapi uvicorn jinja2 python-multipart
```

## Executando
Inicie o servidor com:
```sh
python -m uvicorn main:app --reload
```

A aplicação principal está em [main.py](main.py). As rotas principais implementadas em [main.py](main.py) são:
- [`main.home`](main.py) — rota principal (GET "/") que renderiza [templates/alunos.html](templates/alunos.html)
- [`main.cadastro`](main.py) — tela de cadastro (GET "/cadastro") que renderiza [templates/cadastro.html](templates/cadastro.html)
- [`main.salvar_aluno`](main.py) — endpoint de cadastro (POST "/cadastro") que adiciona alunos
- [`main.atualizar`](main.py) — tela de atualização (GET "/atualizar") que renderiza [templates/atualizar.html](templates/atualizar.html)
- [`main.atualizar_alunos`](main.py) — endpoint de atualização (POST "/atualizar") que atualiza a nota de um aluno

## Estrutura do projeto
- [main.py](main.py) — aplicação FastAPI e lógica das rotas
- templates/
  - [templates/alunos.html](templates/alunos.html)
  - [templates/cadastro.html](templates/cadastro.html)
  - [templates/atualizar.html](templates/atualizar.html)
- static/
  - [static/style.css](static/style.css)

## Observações
- Os templates usam Jinja2 e o diretório de templates é configurado em [main.py](main.py).
- Arquivos estáticos (CSS) são servidos via `/static` conforme `app.mount` em [main.py](main.py).
- Dados de alunos são mantidos em memória na lista `alunos` definida em [main.py](main.py); reiniciar o servidor limpa