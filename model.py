from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    user_name: str
    first_name: str


class User(Model):
    id = fields.IntField(pk=True)
    user_name = fields.CharField(50, unique=True)
    first_name = fields.CharField(50)
    last_name = fields.CharField(50)
    password = fields.CharField(50)
