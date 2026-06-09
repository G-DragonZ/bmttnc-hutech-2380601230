import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '111111111111110'
    data_index = 0

    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            img.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break
    encode_image_path = 'encode_image.png'
    img.save(encode_image_path)
    print("Steganography done. encoded img saved as", encode_image_path)
def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Encode: python encrypt.py encode <image_path> <message> <output_path>")
        print("  Decode: python encrypt.py decode <image_path>")
        return
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path,message)
if __name__ == '__main__':
    main() 