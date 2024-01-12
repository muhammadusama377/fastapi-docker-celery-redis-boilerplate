from pydantic import BaseModel


class Prediction(BaseModel):
    input: str
