# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/main.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'proto/main.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10proto/main.proto\x12\x05unary\"l\n\rCoordinateSet\x12+\n\x0b\x63oordinates\x18\x01 \x03(\x0b\x32\x16.unary.CoordinateArray\x12.\n\x0equery_location\x18\x02 \x01(\x0b\x32\x16.unary.CoordinateArray\"\x1f\n\x0f\x43oordinateArray\x12\x0c\n\x04\x63oor\x18\x01 \x03(\x01\"K\n\x17NearestLocationResponse\x12\x30\n\x10nearest_location\x18\x01 \x01(\x0b\x32\x16.unary.CoordinateArray2T\n\x08Trashify\x12H\n\x0eGetNearestCoor\x12\x14.unary.CoordinateSet\x1a\x1e.unary.NearestLocationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.main_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COORDINATESET']._serialized_start=27
  _globals['_COORDINATESET']._serialized_end=135
  _globals['_COORDINATEARRAY']._serialized_start=137
  _globals['_COORDINATEARRAY']._serialized_end=168
  _globals['_NEARESTLOCATIONRESPONSE']._serialized_start=170
  _globals['_NEARESTLOCATIONRESPONSE']._serialized_end=245
  _globals['_TRASHIFY']._serialized_start=247
  _globals['_TRASHIFY']._serialized_end=331
# @@protoc_insertion_point(module_scope)
