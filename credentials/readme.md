# Credentials
This is a reasonable place to store or inject your certificates and private keys.

## Keystore
Java keystore files are supported by the [maskinporten_auth](../maskinporten_auth) module, and the [example.py](../example.py) file prescribes a file named `certificate_keystore.jks` for this purpose.

## Private/public keys
While the maskinporten authentication client only needs access to a _private_ key, you would need your public key handy for registration in the maskinporten integration portal before use. Keeping both the private and public key on hand here, makes sense at least in a developer environment.

[PEM RSA](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) files are supported by the [maskinporten_auth](../maskinporten_auth) module, and the filename used by the [example.py](../example.py) file is `rsa_private_key.pem`.