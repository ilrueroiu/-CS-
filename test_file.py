import PIL
from PIL import Image, ImageDraw


def user_func(image, x0, y0, x1, y1, fill, width):
    draw = ImageDraw.Draw(image)
    draw.line((x0, y0, x1, y1), fill, width)
    return image


def check_coords(image, x0, y0, x1, y1):
    width, height = image.size

    coord_not_negative = x0 >= 0 and x1 >= 0 and y0 >= 0 and y1 >= 0
    coord_fit = x1 <= width and y1 <= height
    x1y1_greater_x0y0 = x1 > x0 and y1 > y0

    if coord_not_negative and coord_fit and x1y1_greater_x0y0:
        return True
    return False


def set_black_white(image, x0, y0, x1, y1):
    coord_check_not_passed = not (check_coords(image, x0, y0, x1, y1))
    if coord_check_not_passed:
        return image

    grey_image = image.convert('L')
    return grey_image


img = Image.new("RGB", (300, 300), (72, 61, 139))
img = user_func(img, 0, 0, 300, 100, "black", 10)
img = user_func(img, 300, 100, 0, 200, "black", 10)
img = user_func(img, 0, 200, 300, 300, "black", 10)
# img.show()

print(check_coords(img, 0, 1, 2, 10))
img = set_black_white(img, 0, 10, 20, 30)
img.show()
