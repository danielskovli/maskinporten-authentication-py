from typing import Generic, TypeVar
from pydantic import BaseModel, Field, validator

TDetails = TypeVar('TDetails', 'KeystoreCertificateDetails', 'RsaKeyPairDetails')


class KeystoreCertificateDetails(BaseModel):
    cert_store_path: str
    password: str
    key_alias: str


class RsaKeyPairDetails(BaseModel):
    jwk_kid: str
    private_key_pem_path: str


class TokenAuthority(BaseModel):
    issuer: str

    @property
    def token_endpoint(self) -> str:
        return f'{self.issuer.strip("/")}/token'

    def __init__(self, issuer: str):
        '''Shorthand constructor'''
        super().__init__(issuer=issuer)


class TokenRequest(BaseModel, Generic[TDetails]):
    app_id: str
    scopes: list[str] = Field(default_factory=list)
    authority: TokenAuthority
    identification_details: TDetails

    @validator("scopes", pre=True)
    def split_space_separated(cls, o: object):
        '''Allows `scopes` to be initialized with a space-separated string instead of a list'''
        if isinstance(o, str):
            o = o.strip()
            return o.split(" ") if o else []

        return o