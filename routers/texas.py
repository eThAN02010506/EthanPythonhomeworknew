from fastapi import APIRouter

academic_router = APIRouter()



name_list = (
            {"name": "Smith", "number": "240,599", "rank": "1"},
            {"name": "Garcia", "number": "240,333", "rank": "2"},
            {"name": "Rodriguez", "number": "210,765", "rank": "3"},
            {"name": "Johnson", "number": "189,647", "rank": "4"},
            {"name": "Williams", "number": "186,936", "rank": "5"}
)

API_KEYS = [
    "1234567890",
    "qwertyuiop"
]

@academic_router.get("/")
async def get_all_names(api_key: str):
    if api_key in API_KEYS:
        res = []
        for last_name in name_list:
            res.append(last_name['name'])
        return f"The list of most common last names in Texas is: 1. {res[0]} 2. {res[1]} 3. {res[2]} 4. {res[3]} 5. {res[4]}"
    return {"msg": "You do not have permission to access this resource."}


@academic_router.get("/{student_name}")
async def get_student_academic_record(student_name: str):
    return f"{student_name} has a terrible record like Samuel Wu"

