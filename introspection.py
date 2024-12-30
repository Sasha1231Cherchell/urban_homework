from pprint import pprint
from inspect import getmodule


def introspection_info(obj):
    return [
        type(obj).__name__,
        [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        getmodule(obj) if getmodule(obj) is not None else "__main__"
    ]


number_info = introspection_info(42)
pprint(number_info)
