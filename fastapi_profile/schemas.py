from pydantic import BaseModel


class MeasuresOut(BaseModel):
    path: str
    method: str
    headers: dict
    url: str
    query_params: dict
    path_params: dict
    body: dict
    form: dict
    elapsed: float

    class Config:
        orm_mode = True
