from enum import Enum


class ManageAnnulmentOperationType(str, Enum):
    """ManageAnnulmentOperationType -- Technikai érvénytelenítés műveleti típus
    Technical annulment operation type

    """
    # Korábbi adatszolgáltatás technikai érvénytelenítése
    # Technical annulment of previous exchange
    ANNUL = 'ANNUL'
