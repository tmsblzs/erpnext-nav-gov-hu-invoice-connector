from enum import Enum


class QueryOperatorType(str, Enum):
    """QueryOperatorType -- Relációs művelet típus
    Relational operator type

    """
    # Egyenlőség
    # Equals
    EQ = 'EQ'
    # Nagyobb mint reláció
    # Greater than relation
    GT = 'GT'
    # Nagyobb vagy egyenlő reláció
    # Greater or equals relation
    GTE = 'GTE'
    # Kisebb mint reláció
    # Less than relation
    LT = 'LT'
    # Kisebb vagy egyenlő reláció
    # Less or equals relation
    LTE = 'LTE'
