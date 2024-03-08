from . import models


class Defaults:
    '''Default configuration items'''

    class Authority:
        dev = models.TokenAuthority('https://maskinporten.dev/')
        test = models.TokenAuthority('https://test.maskinporten.no/')
        prod = models.TokenAuthority('https://maskinporten.no/')