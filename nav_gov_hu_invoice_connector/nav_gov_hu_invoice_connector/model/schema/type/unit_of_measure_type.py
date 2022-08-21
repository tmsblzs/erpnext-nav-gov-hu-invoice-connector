from enum import Enum


class UnitOfMeasureType(str, Enum):
    """UnitOfMeasureType -- Mennyiség egység típus
    Unit of measure type

    """
    # Darab
    # Piece
    PIECE = 'PIECE'
    # Kilogramm
    # Kilogram
    KILOGRAM = 'KILOGRAM'
    # Metrikus tonna
    # Metric ton
    TON = 'TON'
    # Kilowatt óra
    # Kilowatt hour
    KWH = 'KWH'
    # Nap
    # Day
    DAY = 'DAY'
    # Óra
    # Hour
    HOUR = 'HOUR'
    # Perc
    # Minute
    MINUTE = 'MINUTE'
    # Hónap
    # Month
    MONTH = 'MONTH'
    # Liter
    # Liter
    LITER = 'LITER'
    # Kilométer
    # Kilometer
    KILOMETER = 'KILOMETER'
    # Köbméter
    # Cubic meter
    CUBIC_METER = 'CUBIC_METER'
    # Méter
    # Meter
    METER = 'METER'
    # Folyóméter
    # Linear meter
    LINEAR_METER = 'LINEAR_METER'
    # Karton
    # Carton
    CARTON = 'CARTON'
    # Csomag
    # Pack
    PACK = 'PACK'
    # Saját mennyiségi egység megnevezés
    # Own unit of measure
    OWN = 'OWN'
