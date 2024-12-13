from PIL import Image, ImageFilter

image = Image.open('module_11_1.jpg')
image.show()
image = image.crop((800,400,1200,800)).convert("L").rotate(-12).filter(ImageFilter.SHARPEN)
image.show()