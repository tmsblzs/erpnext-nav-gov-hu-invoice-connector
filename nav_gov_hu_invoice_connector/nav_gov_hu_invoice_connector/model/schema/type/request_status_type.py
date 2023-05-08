from enum import Enum


class RequestStatusType(str, Enum):
    """RequestStatusType -- A kérés feldolgozási státusza
    Processing status of the request

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
    # Feldolgozás befejezve
    # Finished processing
    FINISHED = 'FINISHED'
    # Lekérdezve
    # Notified
    NOTIFIED = 'NOTIFIED'
