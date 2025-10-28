from html import escape

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request, q: str = ""):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "q": q},
    )


@app.get("/healthz")
def healthz():
    return PlainTextResponse("OK")


@app.get("/echo", response_class=HTMLResponse)
def echo(x: str = ""):
    safe_body = "<h1>ECHO</h1><div>you said: {}</div>".format(escape(x, quote=True))
    return HTMLResponse(safe_body)
