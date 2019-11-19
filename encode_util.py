# Licence:CC0 1.0 Universal.
# See Also LICENSE, or <https://creativecommons.org/publicdomain/zero/1.0/legalcode>."


def __bytes_to_2bits(byts):
    bits = []
    for b in byts:
        for mask, shift in zip((0b11000000, 0b110000, 0b1100, 0b11), (6, 4, 2, 0)):
            bits.append((b & mask) >> shift)
    return tuple(bits)


def __bits_to_bytes(bits):
    str_bits = ""
    for b in bits:
        if b == 0:
            str_bits += '00'
        if b == 1:
            str_bits += '01'
        if b == 2:
            str_bits += '10'
        if b == 3:
            str_bits += '11'
    hex_bits = format(int(str_bits, base=2), 'x')
    if len(hex_bits) & 1 == 1:
        hex_bits = "0"+hex_bits
    byts = bytes.fromhex(hex_bits)
    byts = b"\x00" * str_bits.count("00000000", 0,
                                    len(str_bits)-len(str_bits.lstrip("0"))) + byts
    return byts


def encode(byts):
    bits = __bytes_to_2bits(byts)
    bits_encoded = ""
    for b in bits:
        if b == 0:
            bits_encoded += '二'
        if b == 1:
            bits_encoded += '子'
        if b == 2:
            bits_encoded += '玉'
        if b == 3:
            bits_encoded += '舞'
    return bits_encoded


def decode(strings):
    bits = []
    for s in strings:
        if s == '二':
            bits.append(0)
        if s == '子':
            bits.append(1)
        if s == '玉':
            bits.append(2)
        if s == '舞':
            bits.append(3)
    byts = __bits_to_bytes(bits)
    return byts
