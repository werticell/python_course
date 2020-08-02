from collections.abc import Container
from app import VeryImportantClass as VIC, decorator
from numbers import Number


class HackedClass(VIC):
    def __init__(self):
        super().__init__()
        for attribute_name in dir(self):
            attribute = VIC.__getattribute__(self, attribute_name)
            if not attribute_name[0] == '_' and callable(attribute):
                VIC.__setattr__(self, attribute_name, decorator(attribute))

    def __getattribute__(self, attribute_name):
        if attribute_name[0] == '_':
            return VIC.__getattribute__(self, attribute_name)
        else:
            value = VIC.__getattribute__(self, attribute_name)
            if isinstance(value, Number):
                return value * 2
            elif isinstance(value, Container):
                return type(value)()
            else:
                return value
