from enum import Enum


class MarginSchemeType(str, Enum):
    """MarginSchemeType -- Különbözet szerinti szabályozás típus
    Field type for inputting margin-scheme taxation

    """
    # Utazási irodák
    # Travel agencies
    TRAVEL_AGENCY = 'TRAVEL_AGENCY'
    # Használt cikkek
    # Second-hand goods
    SECOND_HAND = 'SECOND_HAND'
    # Műalkotások
    # Works of art
    ARTWORK = 'ARTWORK'
    # Gyűjteménydarabok és régiségek
    # Collector’s items and antiques
    ANTIQUES = 'ANTIQUES'
