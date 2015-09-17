"""Stub file for the '_struct' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import Any, List, Tuple, Dict, Generic

def _clearcache() -> None: ...

def calcsize(*args, **kwargs) -> int: ...

def pack(*args, **kwargs) -> str:
    raise TypeError()

def pack_into(*args, **kwargs) -> None:
    raise TypeError()

def unpack(*args, **kwargs) -> tuple: ...

def unpack_from(*args, **kwargs) -> tuple:
    raise TypeError()


class Struct(object):
    def __sizeof__(self) -> long: ...
    def pack(self, *args, **kwargs) -> str: ...
    def pack_into(self, *args, **kwargs) -> None: ...
    def unpack(self, a) -> tuple: ...
    def unpack_from(self, *args, **kwargs) -> tuple: ...