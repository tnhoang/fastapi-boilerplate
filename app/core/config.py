import secrets
from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "1qwe"
    API_V1_STR: str
    SECRET_KEY: str = secrets.token_urlsafe(32)

    FIRST_SUPERUSER: str
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    @validator("PROJECT_NAME", pre=True)
    def project_name_cant_be_black(cls, v: str) -> Optional[str]:
        return None if len(v) == 0 else v
        # if len(v) == 0:
        #     raise ValueError(v)
        # return v

    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: str

    # @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    # def assemble_db_connection(
    #     cls, v: Optional[str], values: Dict[str, Any]
    # ) -> Any:
    #     if isinstance(v, str):
    #         return v
    #     return PostgresDsn.build(
    #         scheme="postgresql",
    #         user=values.get("POSTGRES_USER"),
    #         password=values.get("POSTGRES_PASSWORD"),
    #         host=values.get("POSTGRES_SERVER"),
    #         path=f"/{values.get('POSTGRES_DB') or ''}",
    #     )

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
