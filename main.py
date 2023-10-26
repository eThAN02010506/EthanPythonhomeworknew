from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routers import texas, last_names

app = FastAPI()

app.include_router(texas.academic_router, prefix="/texas")

app.include_router(last_names.last_name_router, prefix="/last_names")

app.mount("/static", StaticFiles(directory="static"))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
