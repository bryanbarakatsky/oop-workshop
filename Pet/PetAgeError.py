from .PetError import PetError

class PetAgeError(PetError):
    """Custom exception raised when a pet's age is invalid."""
    def __init__(self, message="Invalid pet age"):
        super().__init__(message)
