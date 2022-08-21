from enum import Enum


class SoftwareOperationType(str, Enum):
    """SoftwareOperationType -- A számlázóprogram működési típusa
    (lokális program vagy online számlázó szolgáltatás)
    Billing operation type (local program or online billing service)

    """
    # Lokális program
    # Local program
    LOCAL_SOFTWARE = 'LOCAL_SOFTWARE'
    # Online számlázó szolgáltatás
    # Online billing service
    ONLINE_SERVICE = 'ONLINE_SERVICE'
