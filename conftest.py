import pytest
import requests

from methods_api.users import UsersMethods
from helpers import get_random_user

@pytest.fixture()
def cleanup_user():
    created = {"token": None}

    yield created

    if created["token"]:
        UsersMethods().delete_user(created["token"])

@pytest.fixture()
def logout_user():
    tokens = {"access_token": None, "refresh_token": None}

    yield tokens

    if tokens["access_token"] and tokens["refresh_token"]:
        UsersMethods().post_logout_user(
            tokens["access_token"], tokens["refresh_token"]
        )


@pytest.fixture()
def register_user():
    status, body = UsersMethods().post_register_user(get_random_user())

    access_token = body["accessToken"]

    yield access_token

    if access_token:
        UsersMethods().delete_user(access_token)
