import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException

        if self.validate(name) is None:
            raise DomainException('Invalid domain name.')
        self.name = name

    def validate(self, name_part):
        return re.match(r'.*\.[a-z]{2,3}$', name_part)

    def __str__(self):
        return self.name

    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively
    @classmethod
    def parse_url(cls, url):
        result = url.split('/')[2]
        return cls(result)
    @classmethod
    def parse_email(cls, email):
        result = email.split('@')[1]
        return cls(result)

