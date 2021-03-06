# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import arrai_pb2 as arrai__pb2


class ArraiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Update = channel.stream_stream(
        '/proto.Arrai/Update',
        request_serializer=arrai__pb2.UpdateReq.SerializeToString,
        response_deserializer=arrai__pb2.UpdateAck.FromString,
        )
    self.Observe = channel.unary_stream(
        '/proto.Arrai/Observe',
        request_serializer=arrai__pb2.ObserveReq.SerializeToString,
        response_deserializer=arrai__pb2.ObserveResp.FromString,
        )


class ArraiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Update(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Observe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ArraiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Update': grpc.stream_stream_rpc_method_handler(
          servicer.Update,
          request_deserializer=arrai__pb2.UpdateReq.FromString,
          response_serializer=arrai__pb2.UpdateAck.SerializeToString,
      ),
      'Observe': grpc.unary_stream_rpc_method_handler(
          servicer.Observe,
          request_deserializer=arrai__pb2.ObserveReq.FromString,
          response_serializer=arrai__pb2.ObserveResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Arrai', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
