from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()
templates = Jinja2Templates(directory="templates/Page2")

@router.get("/page2")
async def get_page2(request: Request):
    return templates.TemplateResponse("page2.html", {"request": request})




class User(BaseModel):
    name: str
    age: int
    gender: str

@router.post("/submit")
async def submit_user(user: User):
    return {"name": user.name, "age": user.age, "gender": user.gender}


@router.post("/items")
async def read_item(json_data : dict):
    return JSONResponse(status_code=200 , content={"len":len(json_data['name']), "status": True})


