from Crypto.Hash import SHA3_256
def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.hexdigest()
def main():
    text = input("Enter a message: ").encode('utf-8')
    hashed_text = sha3(text)
    print("SHA3-256 hash:", hashed_text)

if __name__ == "__main__":
    main()