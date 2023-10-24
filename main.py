from fastapi import FastAPI
import uvicorn

from routers import academic, last_name

app = FastAPI()

app.include_router(academic.academic_router, prefix="/academics")

app.include_router(last_name.last_name_router, prefix="/last_names")



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
