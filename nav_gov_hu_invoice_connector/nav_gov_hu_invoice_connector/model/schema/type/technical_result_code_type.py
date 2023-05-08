from enum import Enum


class TechnicalResultCodeType(str, Enum):
    """TechnicalResultCodeType -- Technikai eredmény kód típus
    Technical result code type

    """
    # Kritikus hiba
    # Critical error
    CRITICAL = 'CRITICAL'
    # Hiba
    # Error
    ERROR = 'ERROR'
