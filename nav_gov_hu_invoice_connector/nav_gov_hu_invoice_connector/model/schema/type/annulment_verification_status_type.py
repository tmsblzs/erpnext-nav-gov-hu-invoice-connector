from enum import Enum


class AnnulmentVerificationStatusType(str, Enum):
    """AnnulmentVerificationStatusType -- Technikai érvénytelenítő kérések jóváhagyási státusza
    Verification status of technical annulment requests

    """
    # A technikai érvénytelenítés kliens hiba miatt nem hagyható jóvá
    # The technical annulment is not verifiable due to client error
    NOT_VERIFIABLE = 'NOT_VERIFIABLE'
    # A technikai érvénytelenítés jóváhagyásra vár
    # The technical annulment is awaiting verification
    VERIFICATION_PENDING = 'VERIFICATION_PENDING'
    # A technikai érvénytelenítés jóváhagyásra került
    # The technical annulment has been verified
    VERIFICATION_DONE = 'VERIFICATION_DONE'
    # A technikai érvénytelenítés elutasításra került
    # The technical annulment has been rejected
    VERIFICATION_REJECTED = 'VERIFICATION_REJECTED'
