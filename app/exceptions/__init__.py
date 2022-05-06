class BidsError(Exception):
    def __init__(self, message:dict):
        self.message = message
