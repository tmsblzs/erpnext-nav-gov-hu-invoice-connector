from enum import Enum


class InvoiceDirectionType(str, Enum):
    """InvoiceDirectionType -- Kimenő vagy bejövőszámla keresési paramétere
    Inbound or outbound invoice query parameter

    """
    # Bejövő (vevő oldali) számla keresési paramétere
    # Inbound (customer side) invoice query parameter
    INBOUND = 'INBOUND'
    # Kimenő (kiállító oldali) számla keresési paramétere
    # Outbound (supplier side) invoice query parameter
    OUTBOUND = 'OUTBOUND'
