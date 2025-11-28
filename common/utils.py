import re

from Users.models import User


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+$"

    if re.match(pattern, email):
        return True

    return False