"""
Definitions of extensible but otherwise immutable data structures
"""

import warnings
from typing import Any, Iterable, SupportsIndex


def xi(x: Any) -> Any:
    """
    Make list or dict eXtensible but otherwise Immutable (XI)
    """
    if isinstance(x, list):
        return XiList(x)
    if isinstance(x, dict):
        return XiDict(x)
    return x


class XiList(list):
    """Extensible but otherwise immutable list"""

    def __init__(self, iterable: Iterable) -> None:
        self._data = [xi(x) for x in iterable]
        self.reject_modify_attempt_error_message: str = "XiList (eXtensible but otherwise immutable List) can be extended but not modified"
        
        new_attr_names: set[str] = set(dir(list)).difference(builtin_list_attribute_names)
        if len(new_attr_names) > 0:
            warnings.warn(
                message=(
                    "The following attributes of builtin `list` were not present at time of "
                        "development of XiList, and may compromise immutability and/or extensibility: "
                        f"{new_attr_names}"
                ),
                category=FutureWarning,
                stacklevel=2,
            )
            

    def __add__(self, other):
        """Enables use of `+` with XiList, ensuring the result is also a XiList"""
        if isinstance(other, XiList):
            return XiList(self._data + other._data)
        elif isinstance(other, list):
            return XiList(self._data + other)
        else:
            raise TypeError(
                f"Can only concatenate XiList or iterable, not {type(other).__name__}"
            )

    def __contains__(self, key) -> bool:
        return self._data.__contains__(key)

    def __delattr__(self, name):
        raise TypeError(self.reject_modify_attempt_error_message)

    def __getitem__(self, index_or_slice):
        return self._data.__getitem__(index_or_slice)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"xi{self._data}"

    # def __iter__(self):
    #     """Enables iteration over the XiList."""
    #     return iter(self._data)
    #
    # def __eq__(self, other):
    #     """Checks equality between XiList instances or other iterables."""
    #     if isinstance(other, XiList):
    #         return self._data == other._data
    #     elif isinstance(other, Iterable):
    #         return self._data == list(other)
    #     return False

    def clear(self):
        raise TypeError(self.reject_modify_attempt_error_message)

    def insert(self, index, object):
        raise TypeError(self.reject_modify_attempt_error_message)

    def pop(self, index: SupportsIndex = -1):
        raise TypeError(self.reject_modify_attempt_error_message)

    def remove(self, value):
        raise TypeError(self.reject_modify_attempt_error_message)


class XiDict(dict):
    """Extensible but otherwise immutable dict"""

    def __init__(self, dict_: dict) -> None:
        self._data = {key: xi(value) for key, value in dict_.items()}
        self.reject_modify_attempt_error_message: str = "XiDict (eXtensible but otherwise immutable Dict) can be extended but not modified"

        new_attr_names: set[str] = set(dir(dict)).difference(builtin_dict_attribute_names)
        if len(new_attr_names) > 0:
            warnings.warn(
                message=(
                    "The following attributes of builtin `dict` were not present at time of "
                        "development of XiDict, and may compromise immutability and/or extensibility: "
                        f"{new_attr_names}"
                ),
                category=FutureWarning,
                stacklevel=2,
            )

    def __contains__(self, key) -> bool:
        return self._data.__contains__(key)

    def __delattr__(self, name):
        raise TypeError(self.reject_modify_attempt_error_message)

    def __getitem__(self, key):
        return self._data[key]

    # def __len__(self):
    #     """Returns the number of key-value pairs in the dictionary."""
    #     return len(self._data)
    #
    # def __iter__(self):
    #     """Allows iteration over the keys of the dictionary."""
    #     return iter(self._data)
    #
    # def __contains__(self, key):
    #     """Checks if a key is in the dictionary."""
    #     return key in self._data

    def __getattr__(self, name):
        return self._data[name]

    def __repr__(self):
        """Provides a string representation of the XiDict."""
        return f"xi{self._data}"

    # def __eq__(self, other):
    #     """Checks equality between XiDict and other dictionaries."""
    #     if isinstance(other, XiDict):
    #         return self._data == other._data
    #     elif isinstance(other, dict):
    #         return self._data == other
    #     return False
    #
    # def keys(self):
    #     """Returns a view of the dictionary's keys."""
    #     return self._data.keys()
    #
    # def values(self):
    #     """Returns a view of the dictionary's values."""
    #     return self._data.values()
    #
    # def items(self):
    #     """Returns a view of the dictionary's items."""
    #     return self._data.items()
    #
    # def get(self, key, default=None):
    #     """Returns the value for a key, or a default value if the key is not found."""
    #     return self._data.get(key, default)


builtin_list_attribute_names: set[str] = {
    # generated this list using dir(list) in python 3.13.1
    "__add__",
    "__class__",
    "__class_getitem__",
    "__contains__",
    "__delattr__",
    "__delitem__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__getitem__",
    "__getstate__",
    "__gt__",
    "__hash__",
    "__iadd__",
    "__imul__",
    "__init__",
    "__init_subclass__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__mul__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__reversed__",
    "__rmul__",
    "__setattr__",
    "__setitem__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "append",
    "clear",
    "copy",
    "count",
    "extend",
    "index",
    "insert",
    "pop",
    "remove",
    "reverse",
    "sort",
}

builtin_dict_attribute_names: set[str] = {
    # generated this list using dir(dict) in python 3.13.1
    "__class__",
    "__class_getitem__",
    "__contains__",
    "__delattr__",
    "__delitem__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__getitem__",
    "__getstate__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__ior__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__ne__",
    "__new__",
    "__or__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__reversed__",
    "__ror__",
    "__setattr__",
    "__setitem__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "clear",
    "copy",
    "fromkeys",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
}
