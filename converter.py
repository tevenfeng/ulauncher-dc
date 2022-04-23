def convert_from_binary(number_str):
    """
    :param number_str: number of string to convert
    :return: list including [decimal,octal,hexadecimal]
    """
    decimal = int(number_str, 2)
    octal = oct(decimal)[1:]
    hexadecimal = hex(decimal)[2:].upper()

    return [str(decimal), octal, hexadecimal]


def convert_from_octal(number_str):
    decimal = int(number_str, 8)
    binary = bin(decimal)[2:].zfill(8)
    hexadecimal = hex(decimal)[2:].upper()

    return [binary, str(decimal), hexadecimal]


def convert_from_decimal(number_str):
    binary = bin(int(number_str))[2:].zfill(8)
    octal = oct(int(number_str))[1:]
    hexadecimal = hex(int(number_str))[2:].upper()

    return [binary, octal, hexadecimal]


def convert_from_hexadecimal(number_str):
    decimal = int(number_str, 16)
    binary = bin(decimal)[2:].zfill(8)
    octal = oct(decimal)[1:]

    return [binary, str(decimal), octal]


if __name__ == "__main__":
    number_str = "0xA"
    print(convert_from_hexadecimal(number_str))