from enum import Enum


class TakeoverType(str, Enum):
    """TakeoverType -- Az átvállalás adatait tartalmazó típus
    Field type for data of takeover

    """
    # A 2011. évi LXXXV. tv. 14. § (4) bekezdés szerint az eladó (első belföldi forgalomba hozó) vállalja át a vevő termékdíj-kötelezettségét
    # The supplier takes over buyer’s product fee liability on the basis of Paragraph (4), Section 14 of the Act LXXXV of 2011
    _0_1 = '01'
    # A 2011. évi LXXXV. tv. 14. § (5) aa) alpontja szerint a vevő szerződés alapján átvállalja az eladó termékdíj-kötelezettségét
    # On the basis of contract, the buyer takes over supplier’s product fee liability on the basis of sub-point aa), Paragraph (5), Section 14 of the Act LXXXV of 2011
    _0_2_AA = '02_aa'
    _0_2_AB = '02_ab'
    _0_2_B = '02_b'
    _0_2_C = '02_c'
    _0_2_D = '02_d'
    _0_2_EA = '02_ea'
    _0_2_EB = '02_eb'
    _0_2_FA = '02_fa'
    _0_2_FB = '02_fb'
    _0_2_GA = '02_ga'
    _0_2_GB = '02_gb'
