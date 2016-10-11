from pytesser import *
im = Image.open('photos/one.png')
text = image_to_string(im)
 
print text

im = Image.open('photos/two.tif')
text = image_to_string(im)
 
print text

im = Image.open('photos/three.png')
text = image_to_string(im)
 
print text

im = Image.open('photos/four.png')
text = image_to_string(im)
 
print text

im = Image.open('photos/phototest.tif')
text = image_to_string(im)
 
print text

