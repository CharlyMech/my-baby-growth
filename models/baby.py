from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class Gender(str, Enum):
	MALE = "MALE"
	FEMALE = "FEMALE"


class BirthType(str, Enum):
	VAGINAL = "VAGINAL"
	CESAREAN = "CESAREAN"


class BirthPlace(BaseModel):
	name: str = Field(..., description="Name of the birth place")
	address: str = Field(..., description="Address of the birth place")
	latitude: float = Field(..., description="Latitude of the birth place")
	longitude: float = Field(..., description="Longitude of the birth place")


class Baby(BaseModel):
	id: str = Field(..., description="Unique identifier for the baby")
	name: str = Field(..., description="Name of the baby")
	last_name: str = Field(..., description="Last name of the baby")
	birth_datetime: str = Field(
		..., description="Date and time of birth in YYYY-MM-DD HH:MM format"
	)
	gender: Gender = Field(..., description="Gender of the baby")
	birth_weight_kg: float = Field(..., description="Weight at birth in kilograms")
	birth_height_cm: float = Field(..., description="Height at birth in centimeters")
	birth_head_circum_cm: Optional[float] = Field(
		None, description="Head circumference at birth in centimeters"
	)
	birth_place: BirthPlace | None = Field(..., description="Place of birth")
	birth_type: BirthType = Field(..., description="Type of birth")
