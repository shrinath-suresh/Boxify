# convert bbox values across different formats
from typing import List, Union


def convert_pascal_to_coco(
    annotations: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:
    """
    :param annotations: pascal annotation in form of list. Ex: [[185,11, 307, 132]].
                        Multiple annotations can be passed as [[185,11, 307, 132], [3,6, 183, 163]]
    :return: annotation list in coco format
    :raises ValueError: if annotations are empty
    :raises TypeError: if annotation values are not in list format
    :raises ValueError: if annotation values are not in pascal format
    """
    if len(annotations) == 0:
        raise ValueError(
            "Empty annotation input. Annotation must be in the following format: "
            "[x_min, y_min, x_max, y_max]. Ex: [185,11, 307, 132]."
        )

    coco_annotation: list = []
    for annotation in annotations:
        if isinstance(annotation, list) is not True:
            raise TypeError(
                f"Annotation must be in the following format: "
                f"[x_min, y_min, x_max, y_max]. Ex: [185,11, 307, 132]. But received {annotation}"
            )
        if len(annotation) != 4:
            raise ValueError(
                f"Annotation must be in the following format: [x_min, y_min, x_max, y_max]. "
                f"Ex: [185,11, 307, 132]. But received {annotation}"
            )

        x_min, y_min, x_max, y_max = annotation
        coco_annotation.append([x_min, y_min, (x_max - x_min), (y_max - y_min)])
    return coco_annotation
