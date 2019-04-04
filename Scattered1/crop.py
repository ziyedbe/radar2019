
from PIL import Image
for i in range(1,576):
    imageObject  = Image.open(str(i)+".jpg")

    crop = imageObject.crop((30, 30, 150, 150))
    crop.load() 

    crop.save(str(i), "png")
 
