from typing import Optional

from pydantic import BaseModel


# Shared properties
class ModelBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on model creation
class ModelCreate(ModelBase):
    title: str


# Properties to receive on model update
class ModelUpdate(ModelBase):
    pass


# Properties shared by models stored in DB
class ModelInDBBase(ModelBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Model(ModelInDBBase):
    pass


# Properties properties stored in DB
class ModelInDB(ModelInDBBase):
    pass
