import json

import pytest

from xi import xi, XiDict, XiList

def test_xi_list(): 
    mutable_list: list = [1, 2, [3, 4], 5]
    x = xi(mutable_list)
    assert isinstance(x, XiList)
    assert isinstance(x, list)
    assert x + [1, 2, 3] == xi(mutable_list + [1, 2, 3])
    assert len(x) == len(mutable_list)
    # x.clear()
    # x.insert(index=69, object="test")
    # x.pop()
    # x.pop(2)
    # x.remove(4)
    json.dumps(x, indent=4)
    

def test_xi_dict(): 
    mutable_dict: dict = {
        "a_string": "hello",
        "a_number": 69,
        "a_list": [1, 2, 3],
        "a_dict": {
            "my_name_part1": "j",
            "my_name_part2": "oe",
        },
        "a_nested_thing": [
            {
                "an": {
                    "inner": dict,
                    "meta": "data",
                }
            },
            [69, 420],
        ],
    }
    x = xi(mutable_dict)
    assert isinstance(x, XiDict) 
    assert isinstance(x, dict)
    assert isinstance(x.a_nested_thing[0].an, XiDict)
    assert x.a_list[1] == 2
    assert x.a_dict.my_name_part2 == "oe"

