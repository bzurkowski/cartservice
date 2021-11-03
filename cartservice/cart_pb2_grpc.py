# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cartservice import cart_pb2 as cart__pb2


class CartServiceStub(object):
    """-----------------Cart service-----------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddItem = channel.unary_unary(
                '/hipstershop.CartService/AddItem',
                request_serializer=cart__pb2.AddItemRequest.SerializeToString,
                response_deserializer=cart__pb2.Empty.FromString,
                )
        self.GetCart = channel.unary_unary(
                '/hipstershop.CartService/GetCart',
                request_serializer=cart__pb2.GetCartRequest.SerializeToString,
                response_deserializer=cart__pb2.Cart.FromString,
                )
        self.EmptyCart = channel.unary_unary(
                '/hipstershop.CartService/EmptyCart',
                request_serializer=cart__pb2.EmptyCartRequest.SerializeToString,
                response_deserializer=cart__pb2.Empty.FromString,
                )


class CartServiceServicer(object):
    """-----------------Cart service-----------------

    """

    def AddItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmptyCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CartServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItem,
                    request_deserializer=cart__pb2.AddItemRequest.FromString,
                    response_serializer=cart__pb2.Empty.SerializeToString,
            ),
            'GetCart': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCart,
                    request_deserializer=cart__pb2.GetCartRequest.FromString,
                    response_serializer=cart__pb2.Cart.SerializeToString,
            ),
            'EmptyCart': grpc.unary_unary_rpc_method_handler(
                    servicer.EmptyCart,
                    request_deserializer=cart__pb2.EmptyCartRequest.FromString,
                    response_serializer=cart__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hipstershop.CartService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CartService(object):
    """-----------------Cart service-----------------

    """

    @staticmethod
    def AddItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.CartService/AddItem',
            cart__pb2.AddItemRequest.SerializeToString,
            cart__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.CartService/GetCart',
            cart__pb2.GetCartRequest.SerializeToString,
            cart__pb2.Cart.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EmptyCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.CartService/EmptyCart',
            cart__pb2.EmptyCartRequest.SerializeToString,
            cart__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
