from typing import Annotated

from fastapi import APIRouter, Depends

from auth.keycloak import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/me", summary="Infos utilisateur connecté")
def me(
    user: Annotated[dict, Depends(get_current_user)],
) -> dict:
    """
    Retourne les infos extraites du JWT Keycloak.
    Utile pour tester que l'authentification fonctionne.
    """
    return user
