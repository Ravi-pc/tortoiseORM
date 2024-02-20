from fastapi import FastAPI, HTTPException
from model import User, UserResponse
from schema import UserDetails
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.on_event("startup")
async def startup():
    register_tortoise(
        app,
        db_url='asyncpg://postgres:ra1020@localhost:5432/tortoise_orm',
        modules={'models': ['model']},
        generate_schemas=True
    )


@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserDetails):
    new_user = await User.create(**user.dict())
    return new_user


@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserDetails):
    await User.filter(id=user_id).update(**user.dict())
    updated_user = await User.get_or_none(id=user_id)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User with ID {user_id} deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
