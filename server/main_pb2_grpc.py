# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import main_pb2 as main__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in main_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TrashifyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetNearestCoor = channel.unary_unary(
                '/unary.Trashify/GetNearestCoor',
                request_serializer=main__pb2.CoordinateSet.SerializeToString,
                response_deserializer=main__pb2.NearestLocationResponse.FromString,
                _registered_method=True)


class TrashifyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetNearestCoor(self, request, context):
        """The procedure that will get the nearest coordinates
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrashifyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetNearestCoor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNearestCoor,
                    request_deserializer=main__pb2.CoordinateSet.FromString,
                    response_serializer=main__pb2.NearestLocationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'unary.Trashify', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('unary.Trashify', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Trashify(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetNearestCoor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/unary.Trashify/GetNearestCoor',
            main__pb2.CoordinateSet.SerializeToString,
            main__pb2.NearestLocationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
