"""
Custom Exception Classes for Omni-Store Analytics.
This ensures that we can catch specific errors related to our 
hybrid database architecture.
"""

class OmniStoreError(Exception):
    """Base class for all exceptions in this project."""
    pass

class DatabaseConnectionError(OmniStoreError):
    """Raised when we cannot reach Supabase or MongoDB."""
    def __init__(self, database, message="Failed to connect to"):
        self.database = database
        self.message = f"{message} {self.database}"
        super().__init__(self.message)

class DataNotFoundError(OmniStoreError):
    """Raised when a specific record or file is missing."""
    pass

class ProcessingError(OmniStoreError):
    """Raised when Pandas or NumPy operations fail during analysis."""
    pass