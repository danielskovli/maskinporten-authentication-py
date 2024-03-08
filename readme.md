# Maskinporten authentication library
A small python module that simplifies authentication with Maskinporten, either via enterprise certificates or pre-registered keys.

More information about Maskinporten can be found here: https://samarbeid.digdir.no/maskinporten/maskinporten/25

## Requirements
- A reasonably new version of Python
- Packages as defined in [requirements.txt](requirements.txt)
- A Maskinporten client integration for your target environment

The Maskinporten client must be entitled to grant type `urn:ietf:params:oauth:grant-type:jwt-bearer`, with integration type `maskinporten` and authentication method `private_key_jwt`.

More Maskinporten help: [creating clients](https://docs.digdir.no/docs/Maskinporten/maskinporten_sjolvbetjening_web#opprette-klient-for-%C3%A5-konsumere-api), [registering keys](https://docs.digdir.no/docs/Maskinporten/maskinporten_sjolvbetjening_web#registrere-n%C3%B8kkel-p%C3%A5-klient), [enterprise certificates primer](https://info.altinn.no/en/help/profile/enterprise-certificate/what-are-enterprise-ceritificates) + [registering certificates](https://docs.digdir.no/docs/Maskinporten/maskinporten_sjolvbetjening_web#registrere-sertifikat-p%C3%A5-klient)

## Usage
The [maskinporten_auth](maskinporten_auth) module exposes two primary methods: `authorize_enterprise_cert` and `authorize_key_pair`.

For a complete demo of both methods, please check out [example.py](example.py).

The usage itself is very simple, but some of the surrounding setup can initially be a bit challenging. Primarily in relation to setting up a Maskinporten client and correctly adding a key pair or enterprise certificate. Please refer to the linked docs in the previous section.

In order to run the demo, you must have a certificate keystore and/or private key available and the following environment variables present:
```
# Keystore
CERTIFICATE_CLIENT_ID=...
CERTIFICATE_STORE_PASSWORD=...
CERTIFICATE_KEY_ALIAS=...

# Key pair
# JWKS_CLIENT_ID=...
# JWKS_KID=...

# Common (space separated)
SCOPES=scope1 scope2 scope3
```
:information_source: Side note: The three available Maskinporten environments and associated authority URIs are defined in [config.py](maskinporten_auth/config.py)