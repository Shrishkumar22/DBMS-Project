import pprint
from http.client import HTTPException

from fastapi import FastAPI
from main import locality, admin_data,budget_alloc, sponser, project, login
from pydantic import BaseModel
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from uvicorn import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

# @app.get("/search")
# def find_tribal(name: str):
#     results = list(tribal_memb.find({"name": name}))
#     return [TribalMemb(**result) for result in results]

@app.get("/")
async def hello():
    return "Hello"

@app.get('/login')
async def check(username: str, password: str):
    if login.find_one({"id": username}) is not None:
        data = login.find_one({"id": username})
        if data["password"] == password:
            return {"success": True}
        else:
            return {"success": False}
    else:
        return {"success": False}

# [[Health(**result) for result in result_1], [CounsilMemb(**result) for result in result_2], [
#         BusinessData(**result) for result in result_3], [LocalityData(**result) for result in result_4], [
#         CommunityData(**result) for result in result_5], [TribalMemb(**result) for result in result_6]]

# new api

@app.get("/getall")
def get_data():
    result1 = list(locality.find({}, {"_id": False}))
    result2 = list(project.find({}, {"_id": False}))
    result3 = list(sponser.find({}, {"_id": False}))
    result4 = list(budget_alloc.find({}, {"_id": False}))
    result5 = list(admin_data.find({}, {"_id": False}))
    response_data = {
        "result_1": result1,
        "result_2": result2,
        "result_3": result3,
        "result_4": result4,
        "result_5": result5,
    }
    return response_data


@app.get("/updateproject")
def update(pid: int, value: str):
    update_operation = {
        '$set': {
            'project_name': value,
        }
    }
    try:
        result = project.update_one({'project_id': pid}, update_operation)
        if result.modified_count > 0:
            return {"message": "Project updated successfully"}
        else:
            return {"message": "No matching project found"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/deleteproject")
def deletproject(pid: int):
    project.delete_one({"project_id": pid})


@app.get('/addproject')
def add(pid: int, pname: str, locality: int, admin: int, sponser: int):
    project.insert_one({"project_id": pid,
                            "locality_id": locality,
                            "project_name": pname,
                            "admin_id": admin,
                            "sponsor_id": sponser, })
    return JSONResponse(content={"message": "Successfully added", "success": True})

@app.get('/updatesoner')
def update(sponsor_id: int, new_mobile: str):
    result = sponser.update_one({"sponsor_id": sponsor_id}, {"$set": {"sponsor_mobile": new_mobile}})
    if result.modified_count == 1:
        return {"message": "Sponsor mobile number updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Sponsor not found")

@app.get('/deletesponser')
def delete(sponsor_id: int):
    result = sponser.delete_one({"sponsor_id": sponsor_id})

    if result.deleted_count == 1:
        return {"message": "Sponsor deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Sponsor not found")
