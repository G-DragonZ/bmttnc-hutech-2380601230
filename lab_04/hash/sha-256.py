import hashlib
def calculate_sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()
data_to_hash = input("Enter the data to hash: ")
sha256_hash = calculate_sha256_hash(data_to_hash)
print("SHA-256 hash:", sha256_hash)