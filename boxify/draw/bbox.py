from typing import List, Union, Tuple

from PIL.Image import Image as img

from boxify.constants.formats import Formats
from boxify.formats.pascal import Pascal
from boxify.formats.validate import validate_format


def draw_bbox(
    source_format: str,
    image: Union[str, img],
    annotations: List[List[Union[int, float]]],
    figsize: Tuple[int, int] = (20, 20),
    show: bool = False,
    output_path: str = None,
) -> None:
    """
    :param source_format: Annotation format (yolo, pascal or albumentation)
    :param image: Image URL or path to image
    :param figsize: Matlolib image size
    :param show: Diplay image on screen
    :param output_path: Path to save the image
    """
    validate_format(input_type=source_format)
    if source_format.lower() == Formats.PASCAL.value:

        # First convert pascal to coco format
        pascal = Pascal()
        coco_annotations = pascal.convert_pascal_to_coco(annotations=annotations)

        # Draw bounding box based on coco annotation
        pascal.draw_bounding_box(
            image=image,
            annotations=coco_annotations,
            figsize=figsize,
            show=show,
            output_path=output_path,
        )
