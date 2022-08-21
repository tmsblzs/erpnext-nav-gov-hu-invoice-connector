#
# The super-class for enum types
#

from enum import Enum


class AnnulmentCodeType(str, Enum):
    """AnnulmentCodeType -- Technikai érvénytelenítés kód típusa
    Technical annulment code type

    """
    # Hibás adattartalom miatti technikai érvénytelenítés
    # Technical annulment due to erratic data content
    ERRATIC_DATA = 'ERRATIC_DATA'
    # Hibás számlaszám miatti technikai érvénytelenítés
    # Technical annulment due to erratic invoice number
    ERRATIC_INVOICE_NUMBER = 'ERRATIC_INVOICE_NUMBER'
    # Hibás számla kiállítási dátum miatti technikai érvénytelenítés
    # Technical annulment due to erratic invoice issue date
    ERRATIC_INVOICE_ISSUE_DATE = 'ERRATIC_INVOICE_ISSUE_DATE'
    # Hibás elektronikus számla hash érték miatti technikai érvénytelenítés
    # Technical annulment due to erratic electronic invoice hash value
    ERRATIC_ELECTRONIC_HASH_VALUE = 'ERRATIC_ELECTRONIC_HASH_VALUE'
