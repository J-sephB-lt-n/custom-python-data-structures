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
    for method_name, args in (
        ("clear", tuple()),
        ("insert", (1, "test")),
        ("pop", tuple()),
        ("pop", (2,)),
        ("remove", (4,)),
    ):
        with pytest.raises(TypeError) as raises_data:
            getattr(x, method_name)(*args)
        assert str(raises_data.value) == x.reject_modify_attempt_error_message
    json.dumps(x, indent=4)
    assert 1 in x
    assert 4 in x[2]


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
    assert x.a_string == "hello"
    assert x["a_string"] == "hello"
    assert x.a_list[1] == 2
    assert x["a_list"][1] == 2
    assert x.a_dict.my_name_part2 == "oe"
    assert "a_number" in x
    assert "does not exist" not in x
    assert "data" in x.a_nested_thing[0].an.meta
    assert 80085 not in x.a_nested_thing[1]
    with pytest.raises(TypeError) as raises_data:
        del x.a_string
    assert str(raises_data.value) == x.reject_modify_attempt_error_message
    # with pytest.raises(TypeError) as raises_data:
    #     del x["a_string"]
    # assert str(raises_data.value) == x.reject_modify_attempt_error_message
