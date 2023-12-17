import markdown
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

images_directory = Path("images")
app.mount("/images", StaticFiles(directory=images_directory), name="images")
templates = Jinja2Templates(directory="templates") 


@app.get("/", response_class=HTMLResponse)
def read_home():
    with open(f'./markdown/home.md', "r", encoding="utf-8") as file:
        text_string = file.read()
    
    html = markdown.markdown(text_string, extensions=['attr_list'])
    return templates.TemplateResponse("template.html", { "request": {}, "content": html}, status_code=200)


# Render general content
@app.get("/{path}", response_class=HTMLResponse)
def read_path(path: str):
    try:
        with open(f'./markdown/{path}.md', "r", encoding="utf-8") as file:
            text_string = file.read()

        html = markdown.markdown(text_string, extensions=['attr_list'])
        return templates.TemplateResponse("template.html", { "request": {}, "content": html}, status_code=200)
    except Exception:
        return templates.TemplateResponse("error.html", { "request": {}}, status_code=404)
