from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


def hello():
    return "FastAPI Version 0.68.0"

first = Annotated[str, Depends(hello)]

def get_hello(hello: first):
    return f"Hello, {hello}"

@app.get("/hello")
def dict_hello(message: str = Depends(get_hello)):
    return {"message": message}

