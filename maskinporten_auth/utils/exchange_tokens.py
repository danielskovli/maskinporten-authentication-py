import requests


class Constants:
    grant_type = 'urn:ietf:params:oauth:grant-type:jwt-bearer'


def exchange_tokens(
    token_endpoint: str,
    token: str
) -> dict[str,]:
    '''Exchanges a JWT assertion for an access token using the token endpoint of Maskinporten.'''

    result = requests.post(
        token_endpoint,
        data={
            'grant_type': Constants.grant_type,
            'assertion': token
        }
    )

    return result.json()