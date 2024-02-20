from pydantic import BaseModel


class UserDetails(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    password: str
