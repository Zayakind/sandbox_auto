from enum import Enum

from pydantic import BaseModel, Field


class CompanyStatusEnum(Enum):
    ACTIVE = "ACTIVE"
    BANKRUPT = "BANKRUPT"
    CLOSED = "CLOSED"


class TranslationLang(Enum):
    EN = "EN"
    RU = "RU"
    PL = "PL"
    UA = "UA"


class CompanyDescription(BaseModel):
    translation_lang: TranslationLang
    translation: str


class Company(BaseModel):
    company_id: int = Field(alias="company_id")
    company_name: str = Field(alias="company_name")
    company_address: str = Field(alias="company_address")
    company_status: CompanyStatusEnum = Field(alias="company_status")
    description: str = Field(None, alias="description")
    description_lang: CompanyDescription = Field(None, alias="description_lang")


class User(BaseModel):
    first_name: str = Field(alias="first_name")
    last_name: str = Field(alias="last_name")
    company_id: int = Field(alias="company_id")
    user_id: int = Field(None, alias="user_id")
