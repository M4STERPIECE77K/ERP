from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # URL publique (ce qui apparaît dans le claim 'iss' du JWT)
    keycloak_public_url: str = "http://localhost:8180"
    # URL interne Docker (pour fetcher les JWKS depuis le container FastAPI)
    keycloak_internal_url: str = "http://keycloak:8080"
    keycloak_realm: str = "erp"
    keycloak_client_id: str = "erp-fastapi"
    database_url: str = "oracle+oracledb://erp_user:erp_password@localhost:1521/?service_name=FREEPDB1"

    @property
    def keycloak_issuer(self) -> str:
        # Doit correspondre exactement au claim 'iss' du JWT (URL publique)
        return f"{self.keycloak_public_url}/realms/{self.keycloak_realm}"

    @property
    def keycloak_jwks_uri(self) -> str:
        # Appel interne Docker pour récupérer les clés publiques
        return f"{self.keycloak_internal_url}/realms/{self.keycloak_realm}/protocol/openid-connect/certs"

    model_config = {"env_file": ".env", "extra": "ignore"}

@lru_cache
def get_settings() -> Settings:
    return Settings()
