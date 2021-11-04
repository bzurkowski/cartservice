from concurrent import futures

import grpc
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

from cartservice import cart_pb2, cart_pb2_grpc, cart_service, logger

LOG = logger.get_logger(__name__)

MAX_WORKERS = 1


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    server.add_insecure_port('[::]:7070')

    configure_cart_service(server)
    configure_health_service(server)

    server.start()
    server.wait_for_termination()


def configure_cart_service(server):
    cart_pb2_grpc.add_CartServiceServicer_to_server(
        cart_service.CartService(), server)


def configure_health_service(server):
    health_service = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(
            max_workers=MAX_WORKERS))

    services = cart_pb2.DESCRIPTOR.services_by_name.values()
    service_names = tuple(service.full_name for service in services) + (health.SERVICE_NAME,)

    health_pb2_grpc.add_HealthServicer_to_server(health_service, server)
    for service_name in service_names:
        health_service.set(service_name, health_pb2.HealthCheckResponse.SERVING)


def main():
    LOG.info("Starting Cart Service...")
    serve()
