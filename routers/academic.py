from fastapi import APIRouter

academic_router = APIRouter()

@academic_router.get("/")
async def get_all_academics():
    return "List of all he academics"


@academic_router.get("/{student_name}")
async def get_student_academic_record(student_name: str):
    return f"{student_name} has a terrible record like Samuel Wu"
