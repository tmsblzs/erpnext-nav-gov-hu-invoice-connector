from enum import Enum


class LanguageType(str, Enum):
    """LanguageType -- Nyelv megnevezés típus
    Language naming type

    """
    # Magyar nyelv
    # Hungarian language
    HU = 'HU'
    # Angol nyelv
    # English language
    EN = 'EN'
    # Német nyelv
    # German language
    DE = 'DE'
