# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dwg.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'dwg.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdwg.proto\x12\x04\x66ile\"(\n\tFileChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\x05\"\xac\x01\n\nParameters\x12\x0c\n\x04\x65psg\x18\x01 \x01(\x05\x12\x14\n\x0cnew_center_x\x18\x02 \x01(\x01\x12\x14\n\x0cnew_center_y\x18\x03 \x01(\x01\x12\x12\n\nbbox_min_x\x18\x04 \x01(\x01\x12\x12\n\nbbox_min_y\x18\x05 \x01(\x01\x12\x12\n\nbbox_max_x\x18\x06 \x01(\x01\x12\x12\n\nbbox_max_y\x18\x07 \x01(\x01\x12\x14\n\x0cscale_factor\x18\x08 \x01(\x01\"/\n\rConvertedFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x85\x01\n\x0eUploadResponse\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.file.UploadResponse.Status\x12\"\n\x05\x66iles\x18\x02 \x03(\x0b\x32\x13.file.ConvertedFile\"\"\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\"R\n\rUploadRequest\x12 \n\x06params\x18\x01 \x01(\x0b\x32\x10.file.Parameters\x12\x1f\n\x06\x63hunks\x18\x02 \x03(\x0b\x32\x0f.file.FileChunk2B\n\x0b\x46ileService\x12\x33\n\x06Upload\x12\x13.file.UploadRequest\x1a\x14.file.UploadResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dwg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILECHUNK']._serialized_start=19
  _globals['_FILECHUNK']._serialized_end=59
  _globals['_PARAMETERS']._serialized_start=62
  _globals['_PARAMETERS']._serialized_end=234
  _globals['_CONVERTEDFILE']._serialized_start=236
  _globals['_CONVERTEDFILE']._serialized_end=283
  _globals['_UPLOADRESPONSE']._serialized_start=286
  _globals['_UPLOADRESPONSE']._serialized_end=419
  _globals['_UPLOADRESPONSE_STATUS']._serialized_start=385
  _globals['_UPLOADRESPONSE_STATUS']._serialized_end=419
  _globals['_UPLOADREQUEST']._serialized_start=421
  _globals['_UPLOADREQUEST']._serialized_end=503
  _globals['_FILESERVICE']._serialized_start=505
  _globals['_FILESERVICE']._serialized_end=571
# @@protoc_insertion_point(module_scope)
