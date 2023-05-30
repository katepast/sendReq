from pydantic import BaseModel, validator


class UserSchema(BaseModel):
    company_id: int
    first_name: str
    first_name: str
    user_id: int

    @validator("company_id")
    def check_company_id_is_not_less_zero(cls, company_id_value):
        if company_id_value < 0:
            raise ValueError("Company ID can not be less than zero")
        return company_id_value
