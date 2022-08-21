from enum import Enum


class InvoiceCategoryType(str, Enum):
    """InvoiceCategoryType -- A számla típusa
    Type of invoice

    """
    # Normál (nem egyszerűsített és nem gyűjtő) számla
    # Normal (not simplified and not aggregate) invoice
    NORMAL = 'NORMAL'
    # Egyszerűsített számla
    # Simplified invoice
    SIMPLIFIED = 'SIMPLIFIED'
    # Gyűjtőszámla
    # Aggregate invoice
    AGGREGATE = 'AGGREGATE'
