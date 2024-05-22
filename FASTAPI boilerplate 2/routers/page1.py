from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/Page1")

@router.get("/page1")
async def get_page1(request: Request):
    return templates.TemplateResponse("page1.html", {"request": request})
