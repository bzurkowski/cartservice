import os

from pymongo import MongoClient
from pymongo.write_concern import WriteConcern

from cartservice import cart_pb2, cart_pb2_grpc, logger, exceptions

LOG = logger.get_logger(__name__)


class CartService(cart_pb2_grpc.CartServiceServicer):

    def Connection(self):
        mongodb_url = os.environ.get("MONGODB_URL")
        client = MongoClient(mongodb_url)
        db = client.get_database("hipster", write_concern=WriteConcern(w=3, wtimeout=30000))
        collection = db.carts
        return collection

    def AddItem(self, request, context):
        try:
            LOG.info("Adding item (%s)", request)
            cart_col = self.Connection()
            user_id = request.user_id
            product_id = request.item.product_id
            quantity = request.item.quantity
            cart = cart_col.find_one({"user_id": user_id})
            if not cart:
                cart_item = {"product_id": product_id, "quantity": quantity}
                cart = {"user_id": user_id, "items": [cart_item]}
                cart_col.insert_one(cart)
                return cart_pb2.Empty()
            for item in cart["items"]:
                if item["product_id"] == product_id:
                    item["quantity"] += quantity
            cart_col.replace_one({"user_id": user_id}, cart)
            return cart_pb2.Empty()
        except Exception:
            LOG.error("Unable to access cart storage")
            raise exceptions.CartserviceError("Unable to access cart storage")

    def GetCart(self, request, context):
        try:
            LOG.info("Getting cart (%s)", request)
            cart_col = self.Connection()
            user_id = request.user_id
            cart = cart_col.find_one({"user_id": user_id})
            if cart:
                return cart_pb2.Cart(
                    user_id=user_id,
                    items=[cart_pb2.CartItem(**item) for item in cart["items"]])
            return cart_pb2.Empty()
        except Exception:
            LOG.error("Unable to access cart storage")
            raise exceptions.CartserviceError("Unable to access cart storage")

    def EmptyCart(self, request, context):
        try:
            LOG.info("Removing cart (%s)", request)
            cart_col = self.Connection()
            user_id = request.user_id
            cart = cart_col.find_one({"user_id": user_id})
            if cart:
                cart_col.delete_one({"_id": cart["_id"]})
            return cart_pb2.Empty()
        except Exception as ex:
            LOG.error("Unable to access cart storage: %s", str(ex))
            raise exceptions.CartserviceError("Unable to access cart storage")
