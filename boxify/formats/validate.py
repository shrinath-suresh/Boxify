from boxify.constants.formats import Formats


def validate_format(input_type: str):
    """
    :param input_type: pascal annotation in form of list. Ex: [[185,11, 307, 132]].
    :return: True or False
    :raises ValueError: if input type is not present in format enum
    """
    if input_type.upper() not in Formats.__members__:
        raise ValueError(
            f"Unknown Type {input_type}. Supported types are {Formats.__members__.keys()}"
        )
    else:
        return True
