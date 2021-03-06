# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logging.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='logging.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rlogging.proto\"/\n\x12PostLoggingRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\"%\n\x13PostLoggingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"&\n\x12GetLoggingResponse\x12\x10\n\x08messages\x18\x01 \x03(\t\"\x13\n\x11GetLoggingRequest2~\n\x07Logging\x12\x37\n\ngetLogging\x12\x12.GetLoggingRequest\x1a\x13.GetLoggingResponse\"\x00\x12:\n\x0bpostLogging\x12\x13.PostLoggingRequest\x1a\x14.PostLoggingResponse\"\x00\x62\x06proto3'
)




_POSTLOGGINGREQUEST = _descriptor.Descriptor(
  name='PostLoggingRequest',
  full_name='PostLoggingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='PostLoggingRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='PostLoggingRequest.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=64,
)


_POSTLOGGINGRESPONSE = _descriptor.Descriptor(
  name='PostLoggingResponse',
  full_name='PostLoggingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='PostLoggingResponse.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=103,
)


_GETLOGGINGRESPONSE = _descriptor.Descriptor(
  name='GetLoggingResponse',
  full_name='GetLoggingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='GetLoggingResponse.messages', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=143,
)


_GETLOGGINGREQUEST = _descriptor.Descriptor(
  name='GetLoggingRequest',
  full_name='GetLoggingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['PostLoggingRequest'] = _POSTLOGGINGREQUEST
DESCRIPTOR.message_types_by_name['PostLoggingResponse'] = _POSTLOGGINGRESPONSE
DESCRIPTOR.message_types_by_name['GetLoggingResponse'] = _GETLOGGINGRESPONSE
DESCRIPTOR.message_types_by_name['GetLoggingRequest'] = _GETLOGGINGREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostLoggingRequest = _reflection.GeneratedProtocolMessageType('PostLoggingRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTLOGGINGREQUEST,
  '__module__' : 'logging_pb2'
  # @@protoc_insertion_point(class_scope:PostLoggingRequest)
  })
_sym_db.RegisterMessage(PostLoggingRequest)

PostLoggingResponse = _reflection.GeneratedProtocolMessageType('PostLoggingResponse', (_message.Message,), {
  'DESCRIPTOR' : _POSTLOGGINGRESPONSE,
  '__module__' : 'logging_pb2'
  # @@protoc_insertion_point(class_scope:PostLoggingResponse)
  })
_sym_db.RegisterMessage(PostLoggingResponse)

GetLoggingResponse = _reflection.GeneratedProtocolMessageType('GetLoggingResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGGINGRESPONSE,
  '__module__' : 'logging_pb2'
  # @@protoc_insertion_point(class_scope:GetLoggingResponse)
  })
_sym_db.RegisterMessage(GetLoggingResponse)

GetLoggingRequest = _reflection.GeneratedProtocolMessageType('GetLoggingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGGINGREQUEST,
  '__module__' : 'logging_pb2'
  # @@protoc_insertion_point(class_scope:GetLoggingRequest)
  })
_sym_db.RegisterMessage(GetLoggingRequest)



_LOGGING = _descriptor.ServiceDescriptor(
  name='Logging',
  full_name='Logging',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=166,
  serialized_end=292,
  methods=[
  _descriptor.MethodDescriptor(
    name='getLogging',
    full_name='Logging.getLogging',
    index=0,
    containing_service=None,
    input_type=_GETLOGGINGREQUEST,
    output_type=_GETLOGGINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='postLogging',
    full_name='Logging.postLogging',
    index=1,
    containing_service=None,
    input_type=_POSTLOGGINGREQUEST,
    output_type=_POSTLOGGINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGGING)

DESCRIPTOR.services_by_name['Logging'] = _LOGGING

# @@protoc_insertion_point(module_scope)
