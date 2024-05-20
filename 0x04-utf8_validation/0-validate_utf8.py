#!/usr/bin/python3
""" UTF-8 Validation Module """


def validUTF8(data):
    """ Method that determines if a given
    data set represents a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1s
            while byte & mask:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if num_bytes == 0:
                continue

            # Invalid scenarios
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with 10
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
