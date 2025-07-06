from pydantic import BaseModel
from typing import List
from typing import Optional

class USER_Model(BaseModel):
    user_name  : Optional[str]
    age        : Optional[float]
    experience : Optional[float]
    user_id    : Optional[int]

class UserInfoResponse(BaseModel):
    user_info: List[USER_Model]