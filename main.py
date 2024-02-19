from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from subprocess import Popen, PIPE, STDOUT
import shlex

# Create an instance of the FastAPI class
app = FastAPI()

# Create an instance of Jinja2Templates and specify the directory containing the templates
templates = Jinja2Templates(directory="templates")


def apt_file_search(filename_str: str) -> str:
    """
    Executes 'apt-file search' with the given filename_str and returns the result.
    """
    command = f"apt-file search -i {shlex.quote(filename_str)}"

    process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
    output, _ = process.communicate()

    if process.returncode != 0:
        output = ""

    return [
        (x.split(":")[0], "".join(x.split(":")[1])) for x in output.split("\n") if x
    ]


# Define a path operation that uses a template
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, q: str = None):
    if q:
        output = apt_file_search(q)
    else:
        output = ""

    if q:
        return templates.TemplateResponse(
            "results.html",
            {"request": request, "title": "Apt file search", "output": output, "q": q},
        )
    else:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "title": "Apt file search"},
        )
