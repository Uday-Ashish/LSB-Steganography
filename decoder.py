from PIL import Image

def text_to_binary(text):
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text

def decode_text_from_image(image_path):
    image = Image.open(image_path)
    binary_text = ""

    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y))
            for color_channel in range(3):
                binary_text += format(pixel[color_channel], '08b')[-1]

    delimiter_index = binary_text.find("1111111111111110")
    if delimiter_index != -1:
        binary_text = binary_text[:delimiter_index]

    decoded_text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        decoded_text += chr(int(byte, 2))

    return decoded_text
  
