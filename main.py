from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from subprocess import Popen, PIPE, STDOUT
import shlex

# Create an instance of the FastAPI class
app = FastAPI()


# Define a list of allowed origins for CORS
# You can use "*" to allow all origins or be more specific to enhance security
origins = [
    "http://localhost:8000",  # Allow requests from a local React dev server
    "https://aptfilesearch.oxfordfun.com",  # Adjust to your production React app's domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Or specify just ["GET", "POST"] if you prefer
    allow_headers=["*"],  # You can be more specific depending on your needs
)


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


@app.get("/query_api")
async def read_query_api(q: str = None):
    if q:
        output = {"results": apt_file_search(q)}
    else:
        output = {"results": []}

    return output


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
