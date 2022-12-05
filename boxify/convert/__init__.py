from typing import List, Union

from boxify.constants.formats import Formats
from boxify.formats.pascal import Pascal
from boxify.formats.validate import validate_format


def to_coco(
    source_format: str, annotations: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:
    """
    :param source_format: Annotation format (yolo, pascal or albumentation)
    :param annotations: List of annotations
    :return: Annotation in coco format
    """
    validate_format(input_type=source_format)

    # Pascal to coco
    if source_format.lower() == Formats.PASCAL.value:
        coco_annotations = Pascal().convert_pascal_to_coco(annotations=annotations)
        return coco_annotations

    if source_format.lower() == Formats.YOLO.value:
        raise NotImplemented

    if source_format.lower() == Formats.ALBUMENTATION.value:
        raise NotImplemented
