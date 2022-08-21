from enum import Enum


class BusinessResultCodeType(str, Enum):
    """BusinessResultCodeType -- Üzleti eredmény kód típus
    Business result code type

    """
    # Hiba
    # Error
    ERROR = 'ERROR'
    # Figyelmeztetés
    # Warn
    WARN = 'WARN'
    # Tájékoztatás
    # Information
    INFO = 'INFO'
