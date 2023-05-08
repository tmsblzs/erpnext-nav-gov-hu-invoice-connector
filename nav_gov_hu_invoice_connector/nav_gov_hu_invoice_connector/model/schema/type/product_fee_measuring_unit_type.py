from enum import Enum


class ProductFeeMeasuringUnitType(str, Enum):
    """ProductFeeMeasuringUnitType -- Díjtétel egység típus
    Unit of the rate type

    """
    # Darab
    # Piece
    DARAB = 'DARAB'
    # Kilogramm
    # Kilogram
    KG = 'KG'
