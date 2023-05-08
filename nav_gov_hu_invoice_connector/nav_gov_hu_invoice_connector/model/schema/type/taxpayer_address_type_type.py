from enum import Enum


class TaxpayerAddressTypeType(str, Enum):
    """TaxpayerAddressTypeType -- Adózói cím típus
    Taxpayer address_list type

    """
    # Székhely
    # Headquarter
    HQ = 'HQ'
    # Telephely
    # Site office
    SITE = 'SITE'
    # Fióktelep
    # Branch office
    BRANCH = 'BRANCH'
