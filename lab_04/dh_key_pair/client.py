from cryptography.hazmat.primitives import serialization
def derive_share_secret(private_key, peer_public_key):
    shared_secret = private_key.exchange(peer_public_key)
    return shared_secret
def main():
    with open("public_key.pem", "rb") as f:
        peer_public_key = serialization.load_pem_public_key(f.read())
    parameters = peer_public_key.parameters()
    private_key = parameters.generate_private_key()
    shared_secret = derive_share_secret(private_key, peer_public_key)
    print("Shared secret:", shared_secret.hex())
if __name__ == "__main__":
    main()