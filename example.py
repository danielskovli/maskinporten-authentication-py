from os import path
from pydantic_settings import BaseSettings
import logging
import maskinporten_auth

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s :: %(levelname)-6s :: %(message)s'
)

LOG = logging.getLogger(__name__)


class Environment(BaseSettings):
    '''Runtime environment. Empty values will be fetched from env vars'''

    # Paths
    root_dir: str = path.dirname(__file__)
    credentials_dir: str = path.join(root_dir, 'credentials')
    certificate_store_path: str = path.join(credentials_dir, 'certificate_keystore.jks')
    privatekey_path: str = path.join(credentials_dir, 'rsa_private_key.pem')

    # Secrets
    certificate_client_id: str
    certificate_key_alias: str
    certificate_store_password: str
    jwks_kid: str
    jwks_client_id: str
    scopes: str


class Config:
    '''Configuration for Maskinporten authentication'''

    env = Environment()

    authority = maskinporten_auth.config.Defaults.Authority.dev
    certificate_details = maskinporten_auth.models.KeystoreCertificateDetails(
        cert_store_path=env.certificate_store_path,
        key_alias=env.certificate_key_alias,
        password=env.certificate_store_password
    )
    key_pair_details = maskinporten_auth.models.RsaKeyPairDetails(
        jwk_kid=env.jwks_kid,
        private_key_pem_path=env.privatekey_path
    )


if __name__ == '__main__':
    LOG.info('Authorizing with enterprise certificate...')
    maskinporten_auth.authorize_enterprise_cert(
        maskinporten_auth.models.TokenRequest(
            app_id=Config.env.certificate_client_id,
            scopes=Config.env.scopes,
            authority=Config.authority,
            identification_details=Config.certificate_details
        )
    )

    LOG.info('Authorizing with pre-registered key...')
    maskinporten_auth.authorize_key_pair(
        maskinporten_auth.models.TokenRequest(
            app_id=Config.env.jwks_client_id,
            scopes=Config.env.scopes,
            authority=Config.authority,
            identification_details=Config.key_pair_details
        )
    )
