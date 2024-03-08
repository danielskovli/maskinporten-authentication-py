import logging
from .utils import credentials, generate_token, exchange_tokens
from .models import KeystoreCertificateDetails, RsaKeyPairDetails, TokenRequest

LOG = logging.getLogger(__name__)


def authorize_enterprise_cert(request: TokenRequest[KeystoreCertificateDetails]):
    '''Authorizes with Maskinporten using an enterprise certificate.

    More info about enterprise certificates:
    https://info.altinn.no/en/help/profile/enterprise-certificate/what-are-enterprise-ceritificates
    '''

    pk, cert = credentials.get_key_and_cert(
        request.identification_details.cert_store_path,
        request.identification_details.password,
        request.identification_details.key_alias
    )
    token = generate_token.generate_jwt_x5c(
        request.app_id,
        request.authority.issuer,
        request.scopes,
        cert,
        pk
    )

    return _make_claim(token, request.authority.token_endpoint)


def authorize_key_pair(request: TokenRequest[RsaKeyPairDetails]):
    '''Authorizes with Maskinporten using a pre-registered key pair.

    More information about pre-registered keys:
    https://docs.digdir.no/docs/idporten/oidc/oidc_api_admin#bruk-av-asymmetrisk-n%C3%B8kkel
    '''

    pk = credentials.get_rsa_private_key(
        request.identification_details.private_key_pem_path
    )
    token = generate_token.generate_jwt_kid(
        request.app_id,
        request.authority.issuer,
        request.scopes,
        request.identification_details.jwk_kid,
        pk
    )

    return _make_claim(token, request.authority.token_endpoint)


def _make_claim(token: str, issuer_endpoint: str):
    '''Interal: Sends the actual JWT claim and returns the result'''

    LOG.debug('Generated JWT:')
    LOG.debug(token)

    LOG.debug('Asserting claim with server...')
    result = exchange_tokens.exchange_tokens(
        issuer_endpoint,
        token
    )
    LOG.debug('Server responded:')
    LOG.debug(result)

    return result