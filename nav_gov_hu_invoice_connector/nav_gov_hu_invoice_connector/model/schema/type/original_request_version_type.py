from enum import Enum


class OriginalRequestVersionType(str, Enum):
    """OriginalRequestVersionType -- A lekérdezett számla requestVersion értéke
    Request version value of the queried invoice

    """
    _1_0 = '1.0'
    _1_1 = '1.1'
    _2_0 = '2.0'
    _3_0 = '3.0'
