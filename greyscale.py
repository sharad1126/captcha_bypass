from PIL import Image
img = Image.open('local-filename.jpg').convert('LA')
img.save('greyscale.png')
