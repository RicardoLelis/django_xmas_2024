from pydantic import BaseModel, Field
from pydantic import ValidationError, field_validator


class Weapon(BaseModel):
    name: str = Field(..., description="The weapon name (at least 5 characters)")
    damage: int = Field(..., description="How the weapon create damage")
    weight: int = Field(..., description="The weapon weight (must be a positive integer)")

    @field_validator('name')
    def name_length(cls, v):
        if len(v) < 5:
            raise ValueError('name must be at least 5 characters long')
        return v



try:
    # sword = Weapon(name='Excalibur', damage="too much damage") # raises errors
    sword = Weapon(name='Excalibur', damage=10, weight=100)
except ValidationError as e:
    print(e)


print(Weapon.model_json_schema())