import hashlib

def blake2(message):
    if isinstance(message, str):
        message = message.encode('utf-8')

    blake2b = hashlib.blake2b()
    blake2b.update(message)
    return blake2b.digest()


def blake2_hex(message):
    return blake2(message).hex()


def main():
    text = input('Enter a message: ')
    print('BLAKE2b hash:', blake2_hex(text))


if __name__ == '__main__':
    main()
