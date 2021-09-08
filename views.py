from fastapi import FastAPI, status, HTTPException
from dataclass import TemplateReqDC
from services import SomethingService

app = FastAPI()

service = SomethingService()


@app.get("/")
def get_list():
    return {"message": "Implement me!"}


@app.post("/")
def post_list(req: TemplateReqDC):
    return {"message": f"Implement me {req.num=}!"}


@app.get("/something/{id}")
def get_by_color(id: str):
    return {"message": f"Implement me {id=}!"}


@app.get("/error")
def error_endpoint():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Implement me!")
