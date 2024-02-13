class InvalidKeyException(Exception):
    pass


def _validate_key(key, file1):

    with open(file1, "r") as file:
        content = str(file.read())

    if key <= 1:
        raise InvalidKeyException("Error. Key must be greater than 1.")
    elif key >= len(content):
        raise InvalidKeyException("Error. Key must be less than "
                                  "the length of the file.")
    else:
        return True
