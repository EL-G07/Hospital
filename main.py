# import modules for the app
from fastapi import FastAPI,Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

# app
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory="static"), name='static')

@app.get('/', response_class=HTMLResponse)
def read_root(request:Request):

    return templates.TemplateResponse(request,'index.html')
