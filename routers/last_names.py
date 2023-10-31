from fastapi import APIRouter
from pydantic import BaseModel

last_name_router = APIRouter()


class LastName(BaseModel):
    name: str
    iq: int
    in_america: str


name_list = [
    LastName(name="Jacobs", iq=109, in_america="100 thousand"),
    LastName(name="Acevedo", iq=110, in_america="120 thousand"),
    LastName(name="Mcclain", iq=181, in_america="105 thousand"),
    LastName(name="Burnett", iq=12, in_america="201 thousand"),
    LastName(name="Schitt", iq=112, in_america="190 thousand"),
    LastName(name="Villa", iq=105, in_america="110 thousand"),
    LastName(name="Jones", iq=390, in_america="1"),
    LastName(name="Wolfe", iq=191, in_america="180 thousand"),
    LastName(name="Monroe", iq=101, in_america="95 thousand"),
    LastName(name="Hopkins", iq=151, in_america="230 thousand"),
    LastName(name="Bowers", iq=146, in_america="100 thousand"),
    LastName(name="Daniels", iq=136, in_america="104 thousand"),
    LastName(name="Rivers", iq=90, in_america="114 thousand"),
    LastName(name="Weiss", iq=109, in_america="192 thousand"),
    LastName(name="Olsen", iq=170, in_america="112 thousand"),
    LastName(name="Marsh", iq=130, in_america="103 thousand"),
    LastName(name="Miranda", iq=160, in_america="120 thousand"),
    LastName(name="Wolf", iq=164, in_america="132 thousand"),
    LastName(name="Rasmussen", iq=173, in_america="122 thousand"),
    LastName(name="Rush", iq=100, in_america="107 thousand"),
]



@last_name_router.get("/")
async def get_names(api_key: str):
    if api_key in API_KEYS:
        res = []
        for last_name in name_list:
            res.append(last_name['name'])
        return res
    return {"msg": "You do not have permission to access this resource."}

@last_name_router.get("/{last_name}")
async def get_stats(last_name: str, api_key: str):
    print(api_key)
    if api_key in API_KEYS:
        for name_stats in name_list:
            if last_name.capitalize() == name_stats["name"]:
                return {"name": name_stats['name'], "in_america": name_stats['in_america']}
                # return f"There are {name_stats['in_america']} people in the US with the last name of {name_stats['name']}."
        return {"msg": "Name not found"}
    return {"msg": "You do not have permission to access this resource."}

@last_name_router.get("/{last_name}/average_iq")
async def get_iq(last_name: str, api_key: str):
    if api_key in API_KEYS:
        for name_stats in name_list:
            if last_name.capitalize() == name_stats["name"]:
                return {"name": name_stats['name'], "average_iq": name_stats['iq']}
    return {"msg": "You do not have permission to access this resource."}
