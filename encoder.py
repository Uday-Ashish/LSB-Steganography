def text_to_binary(text):
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text

def encode_text_into_image(image_path, text):
    image = Image.open(image_path)
    binary_text = text_to_binary(text)

    if len(binary_text) > (image.width * image.height * 3):
        raise ValueError("Text too long to be hidden in the given image")

    binary_text += "1111111111111110"  # Adds a delimiter to mark the end of the text

    data_index = 0
    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))
            for color_channel in range(3):
                if data_index < len(binary_text):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_text[data_index], 2)
                    data_index += 1
            image.putpixel((x, y), tuple(pixel))

    encoded_image_path = "encoded_image.png"
    image.save(encoded_image_path)
    return encoded_image_path
  
