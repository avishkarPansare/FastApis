from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import page1, page2

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(page1.router,prefix="/page1")
app.include_router(page2.router,prefix="/page2")

# Templates directory
templates = Jinja2Templates(directory="templates")



if __name__ == "__main__":
    import uvicorn
    # Replace "YOUR_IP_ADDRESS" with your actual IP address
    uvicorn.run(app, host="0.0.0.0", port=8888)