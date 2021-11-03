class CartserviceError(Exception):

    message = "An unknown exception occurred."

    def __init__(self, **kwargs):
        msg = self.message % kwargs
        super(CartserviceError, self).__init__(msg)
