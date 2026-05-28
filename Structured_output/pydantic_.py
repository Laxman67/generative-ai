from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str="Laksh"
    age: Optional[int]=None


user = User()
print(user)
