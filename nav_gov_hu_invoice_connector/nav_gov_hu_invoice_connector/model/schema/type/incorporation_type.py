from enum import Enum


class IncorporationType(str, Enum):
    """IncorporationType -- Gazdasági típus
    Incorporation type

    """
    # Gazdasági társaság
    # Economical company
    ORGANIZATION = 'ORGANIZATION'
    # Egyéni vállalkozó
    # Self employed private entrepreneur
    SELF_EMPLOYED = 'SELF_EMPLOYED'
    # Adószámos magánszemély
    # Private person with tax number
    TAXABLE_PERSON = 'TAXABLE_PERSON'
