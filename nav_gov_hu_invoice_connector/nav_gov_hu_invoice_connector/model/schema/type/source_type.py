from enum import Enum


class SourceType(str, Enum):
    """SourceType -- Az adatszolgáltatás forrása
    Data exchange source

    """
    # Webes adatszolgáltatás
    # Web exchange
    WEB = 'WEB'
    # Kézi XML feltöltés
    # Manual XML upload
    XML = 'XML'
    # Gép-gép adatkapcsolati adatszolgáltatás
    # Machine-to-machine exchange
    MGM = 'MGM'
    # Online pénztárgépes adatszolgáltatás
    # Online cash register exchange
    OPG = 'OPG'
    # NAV online számlázó
    # NTCA online invoicing
    OSZ = 'OSZ'
