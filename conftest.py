import pytest
import requests
from builder.user_builder import UserBuilder
from src.url import COMPANY_URL


@pytest.fixture()
def get_company_url():
    return requests.get(url=COMPANY_URL)


@pytest.fixture()
def get_company_limit_url(request):
    return requests.get(COMPANY_URL + f"?limit={request.param}")


@pytest.fixture()
def generate_user():
    return UserBuilder()

