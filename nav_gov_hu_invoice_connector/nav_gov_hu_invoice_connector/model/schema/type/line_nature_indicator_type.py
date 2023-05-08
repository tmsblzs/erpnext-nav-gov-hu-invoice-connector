from enum import Enum


class LineNatureIndicatorType(str, Enum):
    """LineNatureIndicatorType -- Adott tételsor termékértékesítés vagy szolgáltatás nyújtás jellegének jelzése
    Indication of the nature of the supply of goods or services on a given line

    """
    # Termékértékesítés
    # Supply of goods
    PRODUCT = 'PRODUCT'
    # Szolgáltatás nyújtás
    # Supply of services
    SERVICE = 'SERVICE'
    # Egyéb, nem besorolható
    # Other, non-qualifiable
    OTHER = 'OTHER'
