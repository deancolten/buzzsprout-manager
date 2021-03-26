class ServerError(Exception):
    """Exception for 5xx status codes"""

    def __init__(self, response):
        if response.text:
            self.message = f"{response.status_code} - {response.reason} - {response.text}"
        else:
            self.message = f"{response.status_code} - {response.reason}"
        super().__init__(self.message)


class ClientError(Exception):
    """Exception for 4xx status codes"""

    def __init__(self, response):
        if response.text:
            self.message = f"{response.status_code} - {response.reason} - {response.text}"
        else:
            self.message = f"{response.status_code} - {response.reason}"
        super().__init__(self.message)
