from os import  environ as env
from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
API_KEYS = env.get("API_KEYS").split(",")


texan_router = APIRouter()



class LastName(BaseModel):
    name: str
    number: int
    rank: int
    spanish: str | None = None

name_list = [
            LastName(name="Smith", number=240599, rank=1),
            LastName(name="Garcia", number=240333, rank=2, origin="Spanish"),
            LastName(name="Rodriguez", number=210765, rank=3, origin="Spanish"),
            LastName(name="Johnson", number=189647, rank=4),
            LastName(name="Williams", number=186936, rank=5)
]


# name_list = (
#             {"name": "Smith", "number": "240,599", "rank": "1"},
#             {"name": "Garcia", "number": "240,333", "rank": "2"},
#             {"name": "Rodriguez", "number": "210,765", "rank": "3"},
#             {"name": "Johnson", "number": "189,647", "rank": "4"},
#             {"name": "Williams", "number": "186,936", "rank": "5"}
# )

API_KEYS = [
    "1234567890",
    "qwertyuiop"
]

@texan_router.get("/")
async def get_all_names(api_key: str):
    if api_key in API_KEYS:
        res = []
        for last_name in name_list:
            res.append(last_name.name)
        return f"The list of most common last names in Texas is: 1. {res[0]}, 2. {res[1]}, 3. {res[2]}, 4. {res[3]}, 5. {res[4]}"
    return {"msg": "You do not have permission to access this resource."}


@texan_router.get("/{student_name}")
async def get_student_academic_record(student_name: str):
    return f"{student_name} has a terrible record like Samuel Wu"

