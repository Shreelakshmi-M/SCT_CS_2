from PIL import Image
import random
from google.colab import files

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, path):
    image.save(path)

def swap_pixels(image):
    """Randomly swaps pixel values in the image."""
    pixels = list(image.getdata())
    width, height = image.size

    for _ in range(len(pixels) // 2):
        i, j = random.sample(range(len(pixels)), 2)
        pixels[i], pixels[j] = pixels[j], pixels[i]

    image.putdata(pixels)
    return image

def xor_encrypt(image, key):
    """Applies XOR operation to each pixel with a given key."""
    pixels = list(image.getdata())
    encrypted_pixels = []

    for pixel in pixels:
        if isinstance(pixel, int): 
            encrypted_pixels.append(pixel ^ key)
        else:
            encrypted_pixels.append(tuple(channel ^ key for channel in pixel))

    image.putdata(encrypted_pixels)
    return image

def main():
    input_path = "Capybara-Pictures.jpg"
    image = load_image(input_path)

    operation = input("Choose operation (swap/xor): ").strip().lower()

    if operation == "swap":
        encrypted = swap_pixels(image.copy())
        save_image(encrypted, "encrypted_swap.png")
        print("Image encrypted using pixel swap: saved as 'encrypted_swap.png'")
        files.download("encrypted_swap.png")

    elif operation == "xor":
        key = int(input("Enter XOR key (0-255): "))
        encrypted = xor_encrypt(image.copy(), key)
        save_image(encrypted, "encrypted_xor.png")
        print("Image encrypted using XOR: saved as 'encrypted_xor.png'")
        files.download("encrypted_xor.png")

    else:
        print("Invalid operation. Choose 'swap' or 'xor'.")

# Run the main function
main()
