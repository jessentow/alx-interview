#!/usr/bin/python3
"""UTF-8 validator"""


def validUTF8(data):
    """
      This will Check that a sequence of byte values follows
      the UTF-8 encodingn rules. And does not check for
      canonicalization (i.e. overlong encodings are acceptable).
        """

    data = iter(data)
    for leading_byte in data:
        leading_ones = _counting_leading_ones(leading_byte)
        if leading_ones in [1, 7, 8]:
            return False
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or trailing_byte >> 6 != 0b10:
                return False
    return True


def _counting_leading_ones(byte):
    """This counts the leading ones."""

    for i in range(8):
        if byte >> 7 - i == 0b11111111 >> 7 - i & ~1:
            return i
    return 8
