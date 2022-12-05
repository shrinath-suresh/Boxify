from abc import ABC, abstractmethod


class BaseFormat(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def convert(self, source_format, destination_format):
        pass

    @abstractmethod
    def draw_bounding_box(self, image, annotations, figsize, show):
        pass
