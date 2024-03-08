import jks


def get_key_and_cert(
    keystore_path: str,
    keystore_password: str,
    key_alias: str
):
    '''Returns the private key and certificate from a Java keystore'''

    store = jks.KeyStore.load(
        keystore_path,
        keystore_password
    )
    entry = store.private_keys[key_alias]
    private_key = entry.pkey
    certificate = entry.cert_chain[0][1]

    return private_key, certificate


def get_rsa_private_key(path: str):
    '''Returns the private key from a PEM file'''

    with open(path, 'r') as f:
        return f.read()