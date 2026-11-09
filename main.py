from PIL import Image

chars = ' .:-=+*#%@'

with Image.open("picture.jpg") as image:
    image = image.resize((500, 500))

    for y in range(image.height):
        line = ""
        for x in range(image.width):
            rgb = image.getpixel((x, y))
            grey = sum(rgb) // len(rgb)
            index = grey * 9 // 255
            line += chars[index] + "  "
        print(line)
