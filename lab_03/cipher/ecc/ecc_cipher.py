import os
import ecdsa
from ecdsa import SigningKey, VerifyingKey, BadSignatureError


class ECCCipher:
    def __init__(self, curve=ecdsa.SECP256k1):
        self.curve = curve
        self.keys_dir = os.path.join(os.path.dirname(__file__), "keys")
        os.makedirs(self.keys_dir, exist_ok=True)
        self.private_path = os.path.join(self.keys_dir, "private_key.pem")
        self.public_path = os.path.join(self.keys_dir, "public_key.pem")

    def generate_keys(self):
        sk = SigningKey.generate(curve=self.curve)
        vk = sk.get_verifying_key()
        with open(self.private_path, "wb") as private_file:
            private_file.write(sk.to_pem())
        with open(self.public_path, "wb") as public_file:
            public_file.write(vk.to_pem())
        return sk, vk

    def load_keys(self):
        if not os.path.exists(self.private_path) or not os.path.exists(self.public_path):
            self.generate_keys()

        with open(self.private_path, "rb") as private_file:
            sk = SigningKey.from_pem(private_file.read())
        with open(self.public_path, "rb") as public_file:
            vk = VerifyingKey.from_pem(public_file.read())
        return sk, vk

    def sign(self, message: str, private_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return private_key.sign(message)

    def verify(self, message: str, signature: bytes, public_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        try:
            return public_key.verify(signature, message)
        except BadSignatureError:
            return False