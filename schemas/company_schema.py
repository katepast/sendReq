from pydantic import BaseModel

from enums.company_enum import CompanyActiveStatus


class CompaniesSchema(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyActiveStatus
