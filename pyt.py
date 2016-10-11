from pytesser import *
im = Image.open('my_image.tif') 
text = image_to_string(im) 
print text 