from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoordinateSet(_message.Message):
    __slots__ = ("coordinates", "query_location")
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    QUERY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedCompositeFieldContainer[CoordinateArray]
    query_location: CoordinateArray
    def __init__(self, coordinates: _Optional[_Iterable[_Union[CoordinateArray, _Mapping]]] = ..., query_location: _Optional[_Union[CoordinateArray, _Mapping]] = ...) -> None: ...

class CoordinateArray(_message.Message):
    __slots__ = ("coor",)
    COOR_FIELD_NUMBER: _ClassVar[int]
    coor: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, coor: _Optional[_Iterable[float]] = ...) -> None: ...

class NearestLocationResponse(_message.Message):
    __slots__ = ("nearest_location",)
    NEAREST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    nearest_location: CoordinateArray
    def __init__(self, nearest_location: _Optional[_Union[CoordinateArray, _Mapping]] = ...) -> None: ...
