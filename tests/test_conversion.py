import pytest
from boxify.conversion import convert_pascal_to_coco


def test_pascal_to_coco_empty_conversion_error():
    with pytest.raises(ValueError) as e_info:
        convert_pascal_to_coco(annotations=[])

    assert (
        str(e_info.value) == "Empty annotation input. Annotation must be in the following "
        "format: [x_min, y_min, x_max, y_max]. Ex: [185,11, 307, 132]."
    )


def test_pascal_to_coco_type_conversion_error():
    annotations = [1, 2, 3, 4]
    with pytest.raises(TypeError) as e_info:
        convert_pascal_to_coco(annotations=annotations)

    assert (
        str(e_info.value) == "Annotation must be in the following format: "
        f"[x_min, y_min, x_max, y_max]. Ex: [185,11, 307, 132]. But received {annotations[0]}"
    )


def test_pascal_to_coco_invalid_length_conversion_error():
    annotations = [1, 2, 3, 4, 5, 6]
    with pytest.raises(ValueError) as e_info:
        convert_pascal_to_coco(annotations=[annotations])

    assert (
        str(e_info.value)
        == f"Annotation must be in the following format: [x_min, y_min, x_max, y_max]. "
        f"Ex: [185,11, 307, 132]. But received {annotations}"
    )


def test_pascal_to_coco_single_input():
    annotations = [[185, 11, 307, 132]]
    coco_annotations = convert_pascal_to_coco(annotations=annotations)
    assert coco_annotations == [[185, 11, 122, 121]]


def test_pascal_to_coco_multiple_input():
    annotations = [[185, 11, 307, 132], [3, 6, 183, 163]]
    coco_annotations = convert_pascal_to_coco(annotations=annotations)
    assert coco_annotations == [[185, 11, 122, 121], [3, 6, 180, 157]]
