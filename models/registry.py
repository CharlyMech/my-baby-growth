from pydantic import BaseModel, Field
from typing import Optional


class GrowthRegistry(BaseModel):
	baby_id: str = Field(..., description="Unique identifier for the baby")
	weight_kg: float = Field(..., description="Weight of the baby in kilograms")
	height_cm: Optional[float] = Field(
		..., description="Height of the baby in centimeters"
	)
	head_circum_cm: Optional[float] = Field(
		..., description="Head circumference of the baby in centimeters"
	)
	date: str = Field(
		..., description="Date of the growth measurement in YYYY-MM-DD format"
	)
