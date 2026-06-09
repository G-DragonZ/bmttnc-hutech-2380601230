import base64
def main():
    imput_string = input("Enter a string to encrypt: ")
    encode_bytes = base64.b64encode(imput_string.encode("utf-8"))
    encode_string = encode_bytes.decode("utf-8")
    with open("encrypted.txt", "w") as file:
        file.write(encode_string)
    print("String encrypted and saved to encrypted.txt")
if __name__ == "__main__":    main()