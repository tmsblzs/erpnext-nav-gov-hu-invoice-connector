from enum import Enum


class ProductStreamType(str, Enum):
    """ProductStreamType -- Termékáram típus
    Product stream

    """
    # Akkumulátor
    # Battery
    BATTERY = 'BATTERY'
    # Csomagolószer
    # Packaging products
    PACKAGING = 'PACKAGING'
    # Egyéb kőolajtermék
    # Other petroleum product
    OTHER_PETROL = 'OTHER_PETROL'
    # Az elektromos, elektronikai berendezés
    # The electric appliance, electronic equipment
    ELECTRONIC = 'ELECTRONIC'
    # Gumiabroncs
    # Tire
    TIRE = 'TIRE'
    # Reklámhordozó papír
    # Commercial printing paper
    COMMERCIAL = 'COMMERCIAL'
    # Az egyéb műanyag termék
    # Other plastic product
    PLASTIC = 'PLASTIC'
    # Egyéb vegyipari termék
    # Other chemical product
    OTHER_CHEMICAL = 'OTHER_CHEMICAL'
    # Irodai papír
    # Paper stationery
    PAPER = 'PAPER'
