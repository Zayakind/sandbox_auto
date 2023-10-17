from src.client.http import HttpClient
from src.dataclasses.dataclasses import Company
from src.helpers.common import BASE_ROUTE_COMPANIES, BASE_URL


class CompanyService:

    def __init__(self):
        self.base_route: str = BASE_ROUTE_COMPANIES
        self.http_client = HttpClient(base_url=BASE_URL)

    def get_companies(
        self,
        status: str,
        limit: int = None,
        offset: int = None,
    ) -> list[Company]:
        params = {
            "status": status,
            "limit": limit,
            "offset": offset,
        }
        response = self.http_client.get(
            self.base_route, params=params,
        )
        assert response.status_code == 200
        companies = []
        for company_info in response.json()["data"]:
            companies.append(Company.model_validate(company_info))
        return companies

    def get_company(self, company_id: int) -> Company:
        response = self.http_client.get(
            endpoint=f"{self.base_route}{company_id}"
        )
        assert response.status_code == 200
        company = Company.model_validate(response.json())

        return company