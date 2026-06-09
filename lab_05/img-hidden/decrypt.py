import sys
from PIL import Image

DELIMITER = '111111111111110'  # same delimiter used by the encoder


def convert_binary_to_message(binary_string):
    """Convert binary string to text message."""
    message = ''
    for i in range(0, len(binary_string) - 7, 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            message += chr(int(byte, 2))
    return message


def decode_image(encoded_image_path):
    """Decode and return the hidden message from an encoded image."""
    img = Image.open(encoded_image_path)
    width, height = img.size
    
    pixels = img.load()
    binary_message = ''
    
    # Extract LSB from each pixel's RGB channels
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            # Extract LSB from R, G, B channels
            if len(pixel) >= 3:
                r, g, b = pixel[0], pixel[1], pixel[2]
                binary_message += str(r & 1)
                binary_message += str(g & 1)
                binary_message += str(b & 1)
            
            # Check if we've found the delimiter
            if len(binary_message) >= len(DELIMITER) and binary_message.endswith(DELIMITER):
                # Remove delimiter and convert to message
                binary_message = binary_message[:-len(DELIMITER)]
                return convert_binary_to_message(binary_message)
    
    # If delimiter not found, still try to convert what we have
    return convert_binary_to_message(binary_message)


def main():
    if len(sys.argv) != 2:
        print("usage: python decrypt.py <encoded_image_path>")
        return
    encoded_image_path = sys.argv[1]
    try:
        decode_message = decode_image(encoded_image_path)
        print("Decoded message:", decode_message)
    except Exception as e:
        print("Error decoding image:", e)


if __name__ == "__main__":
    main()