import jwt
import jks
import base64
from uuid import uuid4
from datetime import datetime, timezone, timedelta


class Constants:
    utf8 = 'utf-8'
    rs256 = 'RS256'
    pem_pk_type = 'RSA PRIVATE KEY'


def generate_jwt_x5c(
    app_id: str,
    issuer: str,
    scopes: list[str],
    certificate: bytes,
    private_key: jks.PrivateKeyEntry
):
    '''Generates a JWT assertion for use with Maskinporten,
    using the nationally issued enteriprise certificate'''

    utc_now = datetime.now(tz=timezone.utc)
    claims = {
        'iss': app_id,
        'aud': issuer,
        'scope': ' '.join(scopes),
        'iat': utc_now,
        'exp': utc_now + timedelta(minutes=2),
        'jti': uuid4().__str__()
    }
    headers={
        'x5c': [
            base64.b64encode(certificate).decode(Constants.utf8)
        ]
    }

    return jwt.encode(
        payload=claims,
        headers=headers,
        algorithm=Constants.rs256,
        key=jks.util.as_pem(
            private_key,
            Constants.pem_pk_type
        )
    )


def generate_jwt_kid(
    app_id: str,
    issuer: str,
    scopes: str,
    jwk_kid: str,
    private_key: str
):
    '''Generates a JWT assertion for use with Maskinporten, using a pre-registered key'''

    utc_now = datetime.now(tz=timezone.utc)
    claims = {
        'iss': app_id,
        'aud': issuer,
        'scope': ' '.join(scopes),
        'iat': utc_now,
        'exp': utc_now + timedelta(minutes=2),
        'jti': uuid4().__str__()
    }
    headers={
        'kid': jwk_kid
    }

    return jwt.encode(
        payload=claims,
        headers=headers,
        algorithm=Constants.rs256,
        key=private_key
    )
