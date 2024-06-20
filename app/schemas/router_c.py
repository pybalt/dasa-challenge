from pydantic import BaseModel


class Filter(BaseModel):
    identificador: str
    tipoBusqueda: str
    page: int
    size: int


class RecordDetails(BaseModel):
    ...


class RecordBody(BaseModel):
    filter: Filter
