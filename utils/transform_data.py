"""file to transform data."""


def transform_data(data):
    """Convert list of str in list of int.

    Keyword argument:
    data -- list of str.
    Return:
    list of int.
    """
    list_int = list(map(int, data))
    return list_int
