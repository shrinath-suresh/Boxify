import pytest
from boxify.formats.pascal import Pascal
import PIL
import tempfile
import os
import shutil


def test_pascal_to_coco_empty_conversion_error():
    with pytest.raises(ValueError) as e_info:
        Pascal().convert_pascal_to_coco(annotations=[])

    assert (
        str(e_info.value) == "Empty annotation input. Annotation must be in the following "
        "format: [x_min, y_min, x_max, y_max]. Ex: [185,11, 307, 132]."
    )


def test_pascal_to_coco_type_conversion_error():
    annotations = [1, 2, 3, 4]
    with pytest.raises(TypeError) as e_info:
        Pascal().convert_pascal_to_coco(annotations=annotations)

    assert (
        str(e_info.value) == "Annotation must be in the following format: "
        f"[x_min, y_min, x_max, y_max]. Ex: [185,11, 307, 132]. But received {annotations[0]}"
    )


def test_pascal_to_coco_invalid_length_conversion_error():
    annotations = [1, 2, 3, 4, 5, 6]
    with pytest.raises(ValueError) as e_info:
        Pascal().convert_pascal_to_coco(annotations=[annotations])

    assert (
        str(e_info.value)
        == f"Annotation must be in the following format: [x_min, y_min, x_max, y_max]. "
        f"Ex: [185,11, 307, 132]. But received {annotations}"
    )


def test_pascal_to_coco_single_input():
    annotations = [[185, 11, 307, 132]]
    coco_annotations = Pascal().convert_pascal_to_coco(annotations=annotations)
    assert coco_annotations == [[185, 11, 122, 121]]


def test_pascal_to_coco_multiple_input():
    annotations = [[185, 11, 307, 132], [3, 6, 183, 163]]
    coco_annotations = Pascal().convert_pascal_to_coco(annotations=annotations)
    assert coco_annotations == [[185, 11, 122, 121], [3, 6, 180, 157]]


def test_invalid_image_path():
    path = "dummy_path"
    with pytest.raises(FileNotFoundError, match="Path not found"):
        Pascal().draw_bounding_box(image=path, annotations=[[1, 2, 3, 4]])


def test_invalid_url():
    url = "http://test/test123"

    with pytest.raises(SystemExit):
        Pascal().draw_bounding_box(image=url, annotations=[[1, 2, 3, 4]])


def test_valid_image_local_path():
    image_path = "assets/2007_000027.jpg"
    image = Pascal().draw_bounding_box(image=image_path, annotations=[[169, 104, 209, 146]])

    assert type(image) == PIL.JpegImagePlugin.JpegImageFile


def test_valid_image_url():
    url = "https://thumbs.dreamstime.com/b/cat-dog-26409253.jpg"
    image = Pascal().draw_bounding_box(image=url, annotations=[[169, 104, 209, 146]])

    assert type(image) == PIL.JpegImagePlugin.JpegImageFile


def test_folder_name_as_output_path():
    image_path = "assets/2007_000027.jpg"
    tmp_dir = tempfile.mkdtemp()

    Pascal().draw_bounding_box(image=image_path, annotations=[[169, 104, 209, 146]],
                               output_path=tmp_dir)

    assert "test.jpg" in os.listdir(tmp_dir)
    shutil.rmtree(tmp_dir)


def test_valid_output_path():
    image_path = "assets/2007_000027.jpg"
    tmp_dir = tempfile.mkdtemp()
    output_path = os.path.join(tmp_dir, "test.jpg")

    Pascal().draw_bounding_box(image=image_path, annotations=[[169, 104, 209, 146]],
                               output_path=output_path)

    assert len(os.listdir(tmp_dir)) == 1
    shutil.rmtree(tmp_dir)


def test_valid_output_path_with_name_only():
    image_path = "assets/2007_000027.jpg"
    output_path = "test.jpg"

    Pascal().draw_bounding_box(image=image_path, annotations=[[169, 104, 209, 146]],
                               output_path=output_path)

    assert output_path in os.listdir(os.getcwd())
    os.remove(output_path)
