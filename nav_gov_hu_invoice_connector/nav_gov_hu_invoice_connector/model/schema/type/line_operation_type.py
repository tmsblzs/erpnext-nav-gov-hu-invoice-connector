from enum import Enum


class LineOperationType(str, Enum):
    """LineOperationType -- A számlatétel módosítás típusa
    Invoice line modification type

    """
    CREATE = 'CREATE'
    MODIFY = 'MODIFY'
