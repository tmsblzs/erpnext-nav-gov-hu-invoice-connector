from enum import Enum


class InvoiceAppearanceType(str, Enum):
    """InvoiceAppearanceType -- Számla megjelenési formája típus
    Form of appearance of the invoice type

    """
    # Papír alapú számla
    # Invoice issued on paper
    PAPER = 'PAPER'
    # Elektronikus formában előállított, nem EDI számla
    # Electronic invoice (non-EDI)
    ELECTRONIC = 'ELECTRONIC'
    # EDI számla
    # EDI invoice
    EDI = 'EDI'
    # A szoftver nem képes azonosítani vagy a kiállításkor nem ismert
    # The software cannot be identify the form of appearance of the invoice or it is unknown at the time of issue
    UNKNOWN = 'UNKNOWN'
