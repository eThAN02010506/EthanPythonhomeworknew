from fastapi import FastAPI
import uvicorn

from routers.academic import academic_router
from routers.last_names import last_name_router

app = FastAPI()

app.include_router(academic_router, prefix="/academics")

app.include_router(last_name_router, prefix="/last_name")



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
