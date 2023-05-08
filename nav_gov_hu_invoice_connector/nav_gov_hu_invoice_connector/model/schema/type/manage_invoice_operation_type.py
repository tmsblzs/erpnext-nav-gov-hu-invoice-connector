from enum import Enum


class ManageInvoiceOperationType(str, Enum):
    """ManageInvoiceOperationType -- Számlaművelet típus
    Invoice operation type

    """
    # Adatszolgáltatás eredeti számláról
    # Original invoice exchange
    CREATE = 'CREATE'
    # Adatszolgáltatás az eredeti számlát módosító okiratról
    # Modification invoice exchange
    MODIFY = 'MODIFY'
    # Adatszolgáltatás az eredeti számla érvénytelenítéséről
    # Exchange concerning invoice invalidation
    STORNO = 'STORNO'
