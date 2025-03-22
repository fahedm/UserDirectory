# main.py

from fastapi import FastAPI

from schemas.user import User, SearchUser
from repository import users
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Users"}

@app.post("/add_user/")
async def create_user(user: User):
    a = 'hazra'
    b = 'chachi'
    return a+b

@app.get("/search_users/")
async def search_users(search_user: SearchUser):
    result = users.users()
    return result

@app.get("/modify_users/")
async def search_users(search_user: SearchUser):
    result = users.users()
    return result

@app.get("/display_user/")
async def search_users(search_user: SearchUser):
    result = users.users()
    return result

@app.get("/total_users/")
async def total_users(search_user: SearchUser):
    result = users.users()
    return result

@app.get("/display_user_by_role/")
async def search_users(search_user: SearchUser):
    result = users.users()
    return result

@app.get("/role_info/")
async def search_users(search_user: SearchUser):
    result = users.users()
    return result

@app.get("/delete_user/")
async def search_users(search_user: SearchUser):
    result = users.users()
    return result