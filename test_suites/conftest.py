import pytest

from src.client.service_client import CompanyService


@pytest.fixture()
def company():
    company = CompanyService()
    yield company
