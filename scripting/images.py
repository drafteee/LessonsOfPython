from PIL import Image, ImageFilter

img = Image.open("./scripting/photos/208_astro.jpg")
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert("L")
# # filtered_img.save("grey.png", "png")
# filtered_img.show()
# filtered_img.rotate(90)
# filtered_img.resize((90, 90))
# filtered_img.crop((90, 90, 190, 190))
# filtered_img.save("resize.png", "png")

new_img = img.thumbnail((400, 400))
img.save('thumb2.jpg')
print(img.size)
