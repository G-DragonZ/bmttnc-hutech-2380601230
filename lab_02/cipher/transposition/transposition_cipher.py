class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, plain_text, key):
        if isinstance(key, str):
            key = int(key)
        if key <= 0:
            raise ValueError('key must be a positive integer')

        cipher_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(plain_text):
                cipher_text[col] += plain_text[pointer]
                pointer += key
        return ''.join(cipher_text)

    def decrypt(self, cipher_text, key):
        if isinstance(key, str):
            key = int(key)
        if key <= 0:
            raise ValueError('key must be a positive integer')

        num_of_columns = int(len(cipher_text) / key) + (len(cipher_text) % key > 0)
        num_of_rows = key
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(cipher_text)

        plain_text = [''] * num_of_columns
        column = 0
        row = 0

        for symbol in cipher_text:
            plain_text[column] += symbol
            column += 1

            if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
                column = 0
                row += 1

        return ''.join(plain_text)
