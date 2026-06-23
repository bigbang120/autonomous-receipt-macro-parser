from pydantic import BaseModel


class MacroItem(BaseModel):
    item:str
    calories:float
    protein:float
    carbs:float
    fat:float


class MacroResponse(BaseModel):

    items:list[MacroItem]

    totals:dict
