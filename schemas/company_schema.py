from pydantic import BaseModel


class CompaniesSchema(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: str