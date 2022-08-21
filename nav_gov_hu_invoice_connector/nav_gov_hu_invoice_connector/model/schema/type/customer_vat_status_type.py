from enum import Enum


class CustomerVatStatusType(str, Enum):
    """CustomerVatStatusType -- Vevő ÁFA szerinti státusz típusa
    Customers status type by VAT

    """
    # Belföldi ÁFA alany
    # Domestic VAT subject
    DOMESTIC = 'DOMESTIC'
    # Egyéb (belföldi nem ÁFA alany, nem természetes személy, külföldi ÁFA alany és külföldi nem ÁFA alany, nem természetes személy)
    # Other (domestic non-VAT subject, non-natural person, foreign VAT subject and foreign non-VAT subject, non-natural person)
    OTHER = 'OTHER'
    # Nem ÁFA alany (belföldi vagy külföldi) természetes személy
    # Non-VAT subject (domestic or foreign) natural person
    PRIVATE_PERSON = 'PRIVATE_PERSON'
