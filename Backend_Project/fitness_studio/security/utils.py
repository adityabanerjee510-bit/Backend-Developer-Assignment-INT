from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from fitness_studio.security.auth import verify_token

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth_scheme)):

    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return payload

def get_current_admin(current_user=Depends(get_current_user)):

    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    if current_user.get("emergency", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Emergency login detected. Please change your password first."
        )

    return current_user


def get_emergency_admin(current_user=Depends(get_current_user)):

    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    if not current_user.get("emergency", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This endpoint is only available for emergency login."
        )

    return current_user