"""
This module defines custom exception classes for the application.
"""

class NoMatchingNameError(Exception):
    """Exception raised when no matching name is found in the records."""
    pass

class NoMatchingIdError(Exception):
    """Exception raised when no matching ID is found in the records."""
    pass

class AuthenticationError(Exception):
    """Exception raised when authentication fails."""
    pass

