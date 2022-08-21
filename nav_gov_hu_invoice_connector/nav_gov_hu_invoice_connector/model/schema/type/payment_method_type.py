from enum import Enum


class PaymentMethodType(str, Enum):
    """PaymentMethodType -- Fizetés módja
    Method of payment

    """
    # Banki átutalás
    # Bank transfer
    TRANSFER = 'TRANSFER'
    # Készpénz
    # Cash
    CASH = 'CASH'
    # Bankkártya, hitelkártya, egyéb készpénz helyettesítő eszköz
    # Debit card, credit card, other cash-substitute payment instrument
    CARD = 'CARD'
    # Utalvány, váltó, egyéb pénzhelyettesítő eszköz
    # Voucher, bill of exchange, other non-cash payment instrument
    VOUCHER = 'VOUCHER'
    # Egyéb
    # Other
    OTHER = 'OTHER'
