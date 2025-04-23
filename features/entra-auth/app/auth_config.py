from functools import wraps
from flask import request, jsonify
import jwt
import requests
import os

TENANT_ID = os.getenv("AZURE_TENANT_ID")
AUDIENCE = os.getenv("AZURE_CLIENT_ID")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
JWKS_URL = f"{AUTHORITY}/discovery/v2.0/keys"

jwks = requests.get(JWKS_URL).json()["keys"]

def get_signing_key(kid):
    for key in jwks:
        if key["kid"] == kid:
            return jwt.algorithms.RSAAlgorithm.from_jwk(key)
    return None

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        token = auth_header.replace("Bearer ", "")

        try:
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = get_signing_key(unverified_header["kid"])
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=["RS256"],
                audience=AUDIENCE,
                issuer=f"{AUTHORITY}/v2.0"
            )
        except Exception as e:
            return jsonify({"error": "Unauthorized", "details": str(e)}), 401

        return f(*args, **kwargs)

    return wrapper
