from PIL import Image, ImageFilter
from PIL import ImageEnhance

# Read Image
img = Image.open('cw_1.jpg')

# Display normal image
img.show()

enhanced_img = ImageEnhance.Contrast(img)
# Display enhanced image
enhanced_img.enhance(2.0).show()

