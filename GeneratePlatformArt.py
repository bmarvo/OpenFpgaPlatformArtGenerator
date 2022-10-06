from PIL import Image, ImageOps
import sys

ART_WIDTH = 521
ART_HEIGHT = 165

def apply_transformations(img):
    """
    Apply the required transformations to the image.

    1.) Convert to grayscale
    2.) Rotate 90 degrees ccw
    3.) Invert the image (00 = white, FF = black)
    """
    gray_img = ImageOps.grayscale(img)
    rotated_img = gray_img.rotate(90, expand=1)
    final_img = ImageOps.invert(rotated_img)
    
    return final_img

def main(argv):
    if len(argv) != 1:
        print("Usage: GeneratePlatformArt.py image.png|jpg|bmp|gif")
        sys.exit()

    try:
        img = Image.open(argv[0], 'r')
    except:
        print("Error: Could not open file")
        sys.exit(2)

    width, height = img.size

    # Enforce the resolution requirement
    if width != ART_WIDTH or height != ART_HEIGHT:
        print("Error: The resolution of the image must be 521x165\n")
        sys.exit()

    transformed_img = apply_transformations(img)
    pixel_values = list(transformed_img.getdata())

    out_file_name = argv[0].rsplit('.', 1)[0] + ".bin"
    with open(out_file_name, "wb") as out:
        for pixel in pixel_values:
            out.write(bytes([pixel, 0]))

if __name__ == "__main__":
    main(sys.argv[1:])
