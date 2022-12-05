import os
from io import BytesIO
from typing import List, Union, Tuple
from urllib.parse import urlparse

import matplotlib.patches as patches
import requests
from PIL import Image
from PIL.Image import Image as img
from matplotlib import pyplot as plt

from boxify.base.base_format import BaseFormat


class Pascal(BaseFormat):
    def __init__(self):
        super(Pascal, self).__init__()

    def convert(self, source_format, destination_format):
        pass

    def draw_bounding_box(
        self,
        image: Union[str, img],
        annotations: List[List[Union[int, float]]],
        figsize: Tuple[int, int] = (20, 20),
        show: bool = False,
        output_path: str = None,
    ):
        """
        :param image: Image of type pil.Image
        :param annotations: List of annotations to draw bounding boxes
                            Ex: [ [xmin, ymin, bbox_width, bbox_height], [xmin, ymin, bbox_width, bbox_height]]
        :param figsize: Matplotlib fig size. Defaults to (20, 20)
        :param show: Set it to True to show the plot
        :param output_path: Path to save the image.
                            if output path is specified as folder,
                            output will be written as `test.jpg`, otherwise same filename will be used
        :return: Image of type pil.Image with bounding box drawn
        """
        if isinstance(image, str) and urlparse(image).scheme != "":
            try:
                response = requests.get(image)
                image = Image.open(BytesIO(response.content))
            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                requests.exceptions.Timeout,
                requests.exceptions.RequestException,
            ) as e:
                raise SystemExit(e)
        else:
            if isinstance(image, str) and (not os.path.exists(image)):
                raise FileNotFoundError(f"Path not found - {image}")

            image = Image.open(image)

        fig, ax = plt.subplots(figsize=figsize)

        for annotation in annotations:
            x_min, y_min, bbox_width, bbox_height = annotation

            bb = patches.Rectangle(
                (x_min, y_min),
                bbox_width,
                bbox_height,
                linewidth=2,
                edgecolor="blue",
                facecolor="none",
            )
            ax.add_patch(bb)

        plt.imshow(image)
        if output_path:
            # if user gives a directory, write output to test.jpg inside the dir
            if os.path.isdir(output_path):
                output_path = os.path.join(output_path, "test.jpg")

            plt.savefig(output_path)

        if show:
            plt.show()

        return image

    def convert_pascal_to_coco(
        self, annotations: List[List[Union[int, float]]]
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
                "[x_min, y_min, x_max, y_max]. Ex: [185, 11, 307, 132]."
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
