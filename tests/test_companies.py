import json

import requests

from builder.user_builder import UserBuilder
from schemas.company_schema import CompaniesSchema
from schemas.user_schema import UserSchema
from src.response import Response
import pytest

from src.url import USER_URL


def test_get_companies(get_company_url):
    """Verify received payload corresponds schema and status code eq 200"""
    r = Response(get_company_url)
    r.validate(CompaniesSchema)
    r.assert_status_code(200)


@pytest.mark.parametrize("get_company_limit_url", ["5"], indirect=True)
def test_get_limit_3_companies(get_company_limit_url):
    """Verify received 5 items payload corresponds schema and status code eq 200"""
    r = Response(get_company_limit_url)
    r.validate(CompaniesSchema)
    r.assert_status_code(200)
    print(r)
    assert r.get_length_payload() == 5


def test_create_user():
    """Verify received payload corresponds schema and status code eq 201"""

    post_resp = requests.post(url=USER_URL, data=json.dumps(UserBuilder().response))
    r = Response(post_resp)
    r.validate(UserSchema)
    r.assert_status_code(201)


def test_create_user_with_invalid_company_id():
    """
    Verify inability of creating user with negative company id and
    receiving status code eq 404"""

    resp = requests.post(url=USER_URL, data=json.dumps(UserBuilder().set_company_id(-1).build()))
    r = Response(resp)
    r.validate(UserSchema)
    r.assert_status_code(404)



