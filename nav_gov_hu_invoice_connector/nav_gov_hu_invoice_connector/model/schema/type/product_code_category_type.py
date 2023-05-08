from enum import Enum


class ProductCodeCategoryType(str, Enum):
    """ProductCodeCategoryType -- A termékkód fajtájának jelölésére szolgáló típus
    The type used to mark the kind of product code

    """
    # Vámtarifa szám VTSZ
    # Customs tariff number CTN
    VTSZ = 'VTSZ'
    # Szolgáltatás jegyzék szám SZJ
    # Business service list number BSL
    SZJ = 'SZJ'
    # KN kód (Kombinált Nómenklatúra, 2658/87/EGK rendelet I. melléklete)
    # CN code (Combined Nomenclature, 2658/87/ECC Annex I)
    KN = 'KN'
    # A Jövedéki törvény (2016. évi LXVIII. tv) szerinti e-TKO adminisztratív hivatkozási kódja AHK
    # Administrative reference code of e-TKO defined in the Act LXVIII of 2016 on Excise Duties
    AHK = 'AHK'
    # A termék 343/2011. (XII. 29) Korm. rendelet 1. sz. melléklet A) cím szerinti csomagolószer-katalógus kódja (CsK kód)
    # Packaging product catalogue code of the product according to the Title A) in the Schedule No.1 of the Government Decree No. 343/2011. (XII. 29.)
    CSK = 'CSK'
    # A termék 343/2011. (XII. 29) Korm. rendelet 1. sz. melléklet B) cím szerinti környezetvédelmi termékkódja (Kt kód)
    # Environmental protection product code of the product according to the Title B) in the Schedule No.1 of the Government Decree No. 343/2011. (XII. 29.)
    KT = 'KT'
    # Építményjegyzék szám
    # Classification of Inventory of Construction
    EJ = 'EJ'
    # A Termékek és Szolgáltatások Osztályozási Rendszere (TESZOR) szerinti termékkód - 451/2008/EK rendelet
    # Product code according to the TESZOR (Hungarian Classification of Goods and Services), Classification of Product by Activity, CPA - regulation 451/2008/EC
    TESZOR = 'TESZOR'
    # A vállalkozás által képzett termékkód
    # The own product code of the enterprise
    OWN = 'OWN'
    # Egyéb termékkód
    # Other product code
    OTHER = 'OTHER'
