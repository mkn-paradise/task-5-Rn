from typing import Union, Any
from collections.abc import Iterable, Iterator

""" FieldNames = Union[str, Iterable[str]]

def record_factory(cls_name: str, field_names: FieldNames) -> type[tuple]:

    slots = parse_identifiers(field_names)

    def __init__(self, *args, **kwargs) -> None:
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self) -> Iterator[Any]: 
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self): 
        values = ', '.join(f'{name}={value!r}'
        for name, value in zip(self.__slots__, self))
        cls_name = self.__class__.__name__
        return f'{cls_name}({values})'
    cls_attrs = dict( 
            __slots__=slots,
            __init__=__init__,
            __iter__=__iter__,
            __repr__=__repr__,
    )
    return type(cls_name, (object,), cls_attrs) 
def parse_identifiers(names: FieldNames) -> tuple[str, ...]:
    if isinstance(names, str):
        names = names.replace(',', ' ').split() 
    if not all(s.isidentifier() for s in names):
        raise ValueError('names must all be valid identifiers')
    return tuple(names)
 """


def make_point_class(n, name=None) -> type[tuple]:
    def __init__(self, *args):
        attrs = args
        i = 0
        for value in attrs:
            setattr(self, f"x{i}", value)
            i += 1




class CoordDescriptor:

    def __init__(self, point_name):
        self.point_name = point_name

    def __set__(self, instance, value):
        if isinstance(type(value), int) or isinstance(type(value), float):
            instance.__dict__[self.point_name] = value
        else:
            msg = f"{self.point_name} must be int or float!"
            raise TypeError(msg)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.point_name]



