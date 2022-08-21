from enum import Enum


class InvoiceStatusType(str, Enum):
    """InvoiceStatusType -- A számla feldolgozási státusza
    Processing status of the invoice

    """
    # Befogadva
    # Received
    RECEIVED = 'RECEIVED'
    # Feldolgozás alatt
    # Processing
    PROCESSING = 'PROCESSING'
    # Elmentve
    # Saved
    SAVED = 'SAVED'
    # Kész
    # Done
    DONE = 'DONE'
    # Kihagyva
    # Aborted
    ABORTED = 'ABORTED'
