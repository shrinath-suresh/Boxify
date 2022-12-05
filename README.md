# Boxify
convert and draw bounding boxes in Pascal, Albumentation, coco and yolo formats

## Convert to other formats using python api

Convert pascal to coco

``` python
from boxify.convert import to_coco
coco_annotations = to_coco(source_format="pascal", annotations=[[169, 104, 209, 146]])
```

output

```
[[169, 104, 40, 42]]
```

## Draw bounding box on image (show image/ save image)

``` python
from boxify.draw.bbox import draw_bbox

draw_bbox(source_format="pascal", image=<path to image>, annotations=[[169, 104, 209, 146]], show=True, output_path=<path to save the file>)
```

image - Path can either be local path or a valid URL
show - To show matplotlib image, set it to True.
output_path - Local path to save the image. If target is a directory, the file is saved as `test.jpg`
