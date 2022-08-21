from enum import Enum


class FunctionCodeType(str, Enum):
    """FunctionCodeType -- Funkciókód típus
    Function code type

    """
    # Sikeres művelet
    # Successful operation
    OK = 'OK'
    # Hiba
    # Error
    ERROR = 'ERROR'
