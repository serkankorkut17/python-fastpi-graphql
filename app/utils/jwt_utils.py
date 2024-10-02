import os
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv
from fastapi import HTTPException


load_dotenv("../../.env")

# Ensure the SECRET_KEY is set and handle the error if it's missing
secret_key = os.getenv("SECRET_KEY")
if not secret_key:
    raise ValueError("SECRET_KEY not found in environment variables")

# JWT algorithm
algorithm = (
    "HS256"  # For stronger security, consider using RS256 with private/public key pairs
)
issuer = "serkankorkut.dev"  # Set your app name or domain
audience = "serkankorkut.dev/users"  # Define the expected audience, e.g., your users


def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a JWT access token.

    :param data: The payload to encode in the token.
    :param expires_delta: Optional expiration timedelta for the token.
    :param audience: Optional audience claim to include in the token.
    :param issuer: Optional issuer claim to include in the token.
    :return: Encoded JWT token as a string.
    """
    to_encode = data.copy()
    expire = datetime.now() + (
        expires_delta or timedelta(minutes=30)
    )  # Default to 30 minutes if no expiration provided
    to_encode.update({"exp": expire, "aud": audience, "iss": issuer})
    access_token = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return access_token


def decode_access_token(token: str):
    """
    Decodes and validates a JWT token.

    :param token: The JWT token to decode.
    :param audience: Optional audience claim to validate.
    :param issuer: Optional issuer claim to validate.
    :return: Decoded token data.
    :raises HTTPException: If the token is invalid or expired.
    """
    try:
        token_data = jwt.decode(
            token, secret_key, algorithms=[algorithm], audience=audience, issuer=issuer
        )
        return token_data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
