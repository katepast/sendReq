from schemas.company_schema import CompaniesSchema
from src.response import Response


def test_companies(get_company_url):
    r = Response(get_company_url)
    r.validate(CompaniesSchema)
    r.assert_status_code(200)


