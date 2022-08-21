from enum import Enum


class ProductFeeOperationType(str, Enum):
    """ProductFeeOperationType -- Termékdíj-összesítés típus
    Product fee summary type

    """
    # Visszaigénylés
    # Refund
    REFUND = 'REFUND'
    # Raktárba szállítás
    # Deposit
    DEPOSIT = 'DEPOSIT'
