import pytest

from src.client.service_client import CompanyService


class TestResponseBase:

    @pytest.mark.parametrize(
        "status, limit, offset", [
            ("ACTIVE", 3, 0),
            ("BANKRUPT", 5, 2),
            ("CLOSED", 12, 3),
        ]
    )
    def test_get_status_company(
        self,
        company: CompanyService,
        status: str,
        limit: int,
        offset: int,
    ):
        companies = company.get_companies(
            status=status, limit=limit, offset=offset
        )

        for company in companies:
            assert status == company.company_status.value
