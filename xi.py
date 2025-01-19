"""
Definitions of extensible but otherwise immutable data structures
"""

from typing import Any, Iterable

def xi(x: Any) -> Any:
    """
    TODO
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


class XiDict(dict):
    """Extensible but otherwise immutable dict"""

    def __init__(self, dict_: dict) -> None:
        self._data = {key: xi(value) for key, value in dict_.items()}
        self.reject_modify_attempt_error_message: str = "XiDict (eXtensible but otherwise immutable Dict) can be extended but not modified"

    # def __getitem__(self, key):
    #     """Allows access to items using the key."""
    #     return self._data[key]
    #
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
