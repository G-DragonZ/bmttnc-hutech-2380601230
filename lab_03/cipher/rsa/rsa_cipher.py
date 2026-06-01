import os

import rsa


class RSACipher:
    def __init__(self, key_size: int = 2048):
        self.key_size = key_size
        self.keys_dir = os.path.join(os.path.dirname(__file__), "keys")
        os.makedirs(self.keys_dir, exist_ok=True)
        self.private_path = os.path.join(self.keys_dir, "private_key.pem")
        self.public_path = os.path.join(self.keys_dir, "public_key.pem")

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(self.key_size)
        with open(self.private_path, "wb") as private_file:
            private_file.write(private_key.save_pkcs1("PEM"))
        with open(self.public_path, "wb") as public_file:
            public_file.write(public_key.save_pkcs1("PEM"))
        return private_key, public_key

    def load_keys(self):
        if not os.path.exists(self.private_path) or not os.path.exists(self.public_path):
            self.generate_keys()

        with open(self.private_path, "rb") as private_file:
            private_data = private_file.read()
        with open(self.public_path, "rb") as public_file:
            public_data = public_file.read()

        private_key = rsa.PrivateKey.load_pkcs1(private_data)
        public_key = rsa.PublicKey.load_pkcs1(public_data)
        return private_key, public_key

    def encrypt(self, message: str, key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return rsa.encrypt(message, key)

    def decrypt(self, ciphertext: bytes, key):
        decrypted = rsa.decrypt(ciphertext, key)
        return decrypted.decode("utf-8")

    def sign(self, message: str, private_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return rsa.sign(message, private_key, "SHA-256")

    def verify(self, message: str, signature: bytes, public_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        try:
            rsa.verify(message, signature, public_key)
            return True
        except rsa.VerificationError:
            return False
