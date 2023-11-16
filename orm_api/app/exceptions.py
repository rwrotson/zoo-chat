class BestiaryNotFound(Exception):
    """Raised when there are no bestiary with given title yet"""
    pass


class BestiaryAlreadyExists(Exception):
    """Raised when there are already bestiary with given title"""
    pass


class UserNotFound(Exception):
    """Raised when there are no such user in database"""
    pass


class UserAlreadyExists(Exception):
    """Raised when there are already bestiary with given title"""
    pass
