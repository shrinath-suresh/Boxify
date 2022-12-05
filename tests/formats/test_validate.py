import pytest
from boxify.formats.validate import validate_format


def test_invalid_format():
    input_str = "test"
    with pytest.raises(ValueError, match="Unknown Type"):
        validate_format(input_type=input_str)


@pytest.mark.parametrize("input_str", ["yolo", "coco", "pascal", "albumentation"])
def test_valid_format(input_str):
    assert True is validate_format(input_type=input_str)
