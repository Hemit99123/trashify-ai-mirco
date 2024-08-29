from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoordinateSet(_message.Message):
    __slots__ = ("coordinates", "query_location")
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    QUERY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedCompositeFieldContainer[Coordinate]
    query_location: Coordinate
    def __init__(self, coordinates: _Optional[_Iterable[_Union[Coordinate, _Mapping]]] = ..., query_location: _Optional[_Union[Coordinate, _Mapping]] = ...) -> None: ...

class Coordinate(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class NearestLocationResponse(_message.Message):
    __slots__ = ("nearest_location", "distance")
    NEAREST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    nearest_location: Coordinate
    distance: float
    def __init__(self, nearest_location: _Optional[_Union[Coordinate, _Mapping]] = ..., distance: _Optional[float] = ...) -> None: ...
