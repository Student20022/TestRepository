import pytest
from Collections.collection_task import once_presented_chars_num

valid_case = [
    ("abbbccdf", 3),
    ("asdfdsg", 3),
    ("dsadsa", 0),
    ("21325.", 4)

]


@pytest.mark.parametrize('data, result', valid_case)
def test_validation(data, result):
    assert once_presented_chars_num(data) == result


def test_type():
    with pytest.raises(TypeError):
        once_presented_chars_num(12332)
