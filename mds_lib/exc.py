"""
Exceptions
"""


class MDSException(Exception):
    """Main Exception"""


class MDSConfigException(MDSException):
    """
    Exception with config mds lib
    """

    def __init__(self):
        self.message = "Not Found config for executable"
        Exception.__init__(self, self.message)


class MDSHostException(MDSException):
    """In provided incorrect mds host"""

    def __init__(self, incorrect_host: str):  # pragma: no cover
        self.message = (
            f"Invalid host - `{incorrect_host}`." f" Please check config data"
        )
        Exception.__init__(self, self.message)


class MDSRequestException(MDSException):
    """Errors with http requests"""

    def __init__(self, request_type, bad_response: str):
        self.message = f"Request: {request_type} returned error. Error: {bad_response}"
        Exception.__init__(self, self.message)


class NotAllowedMethods(MDSException):
    """ """

    def __init__(
        self, incorrect_method: str, allowed_methods: list[str]
    ):  # pragma: no cover
        self.message = (
            f"NotAllowedMethod - `{incorrect_method}`."
            f" AllowedMethods - {allowed_methods}"
        )
        Exception.__init__(self, self.message)
