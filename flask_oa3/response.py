class APIResponse:
    def __init__(self, status_code=None, data=None):
        self.status_code = status_code
        self.data = data