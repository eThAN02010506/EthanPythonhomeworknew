from fastapi import FastAPI
import uvicorn

app = FastAPI()

API_KEYS = [
    "1234567890",
    "qwertyuiop"
]

name_list = [
    {"name": "Jacobs", "iq": 109, "in_america": "100 thousand"},
    {"name": "Acevedo", "iq": 110, "in_america": "120 thousand"},
    {"name": "Mcclain", "iq": 181, "in_america": "105 thousand"},
    {"name": "Burnett", "iq": 12, "in_america": "201 thousand"},
    {"name": "Schitt", "iq": 112, "in_america": "190 thousand"},
    {"name": "Villa", "iq": 105, "in_america": "110 thousand"},
    {"name": "Jones", "iq": 390, "in_america": "1"},
    {"name": "Wolfe", "iq": 191, "in_america": "180 thousand"},
    {"name": "Monroe", "iq": 101, "in_america": "95 thousand"},
    {"name": "Hopkins", "iq": 151, "in_america": "230 thousand"},
    {"name": "Bowers", "iq": 146, "in_america": "100 thousand"},
    {"name": "Daniels", "iq": 136, "in_america": "104 thousand"},
    {"name": "Rivers", "iq": 90, "in_america": "114 thousand"},
    {"name": "Weiss", "iq": 109, "in_america": "192 thousand"},
    {"name": "Olsen", "iq": 170, "in_america": "112 thousand"},
    {"name": "Marsh", "iq": 130, "in_america": "103 thousand"},
    {"name": "Miranda", "iq": 160, "in_america": "120 thousand"},
    {"name": "Wolf", "iq": 164, "in_america": "132 thousand"},
    {"name": "Rasmussen", "iq": 173, "in_america": "122 thousand"},
    {"name": "Rush", "iq": 100, "in_america": "107 thousand"}
]

@app.get("/top20-last-names")
async def get_names(api_key: str):
    if api_key in API_KEYS:
        res = []
        for last_name in name_list:
            res.append(last_name['name'])
        return res
    return {"msg": "You do not have permission to access this resource."}

@app.get("/top20-last-names/{last_name}")
async def get_stats(last_name: str, api_key: str):
    print(api_key)
    if api_key in API_KEYS:
        for name_stats in name_list:
            if last_name.capitalize() == name_stats["name"]:
                return f"There are {name_stats['in_america']} people in the US with the last name of {name_stats['name']}."
        return {"msg": "Name not found"}
    return {"msg": "You do not have permission to access this resource."}

@app.get("/top20-last-names/{last_name}/average_iq")
async def get_iq(last_name: str, api_key: str):
    if api_key in API_KEYS:
        for name_stats in name_list:
            if last_name.capitalize() == name_stats["name"]:
                return f"People in the US with the last name of {name_stats['name']} have an average iq of {name_stats['iq']}"
    return {"msg": "You do not have permission to access this resource."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
