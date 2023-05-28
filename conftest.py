import pytest
import requests
from src.url import COMPANY_URL


@pytest.fixture()
def get_company_url():
    return requests.get(COMPANY_URL)
