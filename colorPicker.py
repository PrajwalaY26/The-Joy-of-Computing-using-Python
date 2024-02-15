#here we will write a program to pick a RGB format from an image

#import image library from PIL


from PIL import Image as i
im=i.open("RGB-Format.png");
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((150,1))
print(r,g,b)