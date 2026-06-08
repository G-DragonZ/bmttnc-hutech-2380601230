import math

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

# MD5 implementation based on RFC 1321
def md5(message):
    if isinstance(message, str):
        message = message.encode('utf-8')

    # Initialize variables:
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Per-round shift amounts
    s = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21,
    ]

    # Use integer part of sines of integers (in radians) as constants:
    K = [int(abs(math.sin(i + 1)) * (1 << 32)) & 0xFFFFFFFF for i in range(64)]

    original_length_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length_bits.to_bytes(8, byteorder='little')

    for chunk_start in range(0, len(message), 64):
        chunk = message[chunk_start:chunk_start + 64]
        M = [int.from_bytes(chunk[i:i + 4], byteorder='little') for i in range(0, 64, 4)]

        A = a0
        B = b0
        C = c0
        D = d0

        for i in range(64):
            if 0 <= i <= 15:
                F = (B & C) | ((~B) & D)
                g = i
            elif 16 <= i <= 31:
                F = (D & B) | ((~D) & C)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                F = C ^ (B | (~D))
                g = (7 * i) % 16

            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + left_rotate(F, s[i])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    digest = (a0.to_bytes(4, byteorder='little') +
              b0.to_bytes(4, byteorder='little') +
              c0.to_bytes(4, byteorder='little') +
              d0.to_bytes(4, byteorder='little'))
    return digest


def md5_hex(message):
    return md5(message).hex()


def main():
    input_string = input("Enter a string: ")
    print("MD5 hash:", md5_hex(input_string))


if __name__ == "__main__":
    main()

