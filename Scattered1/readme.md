# Scattered1

Description : A lot of scattered pictures , do you think they give you a secret ? 

## Walkthrough

We were given 576 pictures, on each of them written a caracter. I went through some of the images and figured out it's a base64 code. So the real challenge was extracting all the letters.

To do that, i looked all around the internet and found a great tool called pytesseract. 
Using it directly on the images didn't give accurate output. So i used a script to crop all the images.


```python
from PIL import Image
for i in range(1,576):
    imageObject  = Image.open(str(i)+".jpg")

    crop = imageObject.crop((30, 30, 150, 150))
    crop.load() 

    crop.save(str(i), "png")
```

After cropping all the images i run this script

```python
import pytesseract
ch=""
for i in range(1,576):
    out= pytesseract.image_to_string(str(i),config='--psm 10')
    if out =="":
        ch+="a"
    elif out =="|":
        ch+="l"
    else:
        ch+=out[0]
print(ch)
```
The first condition is used to add a padding in case pytesseract wasn't able to detect the caracter.
Second condition was because pytesseract detect "l" as "|"

Output
```bash
SGVSbG8gYWdhaW4gLCB3b3UgZGlklGEgZ29VZCBqb2lgd293lGFUZCBIZWNhdXNllHlVdSBkaWQgYSBnb29klGpVYIBhbmQgeW91lGNhbIBmaW3klHlVdXlgZmXhZyBpbIB0aGUgZW3klG9mlHRleHQgLCBnb29klGX1Y2SgYW3klGRVbId0lGZVCmdldCB0byB0YWtllGEgCmVZdCBhbmQgaGF2ZSBhlGdVb2QgbmlnaHQgYmVaYXVZZSB3b3UgYXJllGdVb2QgCHJVZ3JhbW1lCIBhbmQgZG9UJ3QgZm9yZ2V0lHRVlHN1Ym1pdCB0aGUgZmXhZyBhbmQgeWVZlHllCyBJlHdhbnQgdG8gbWFrZSB0aGUgYmFZZTY0lHZlCnkgbG9UZyBIZWNhdXNllEkgd2FUdCB0byBaCmVhdGUgYSBSb3Qgb2YgCGhVdG9ZlGJlY2F1C2UgdGhllGXhenp3lHBlb3BSZSBmaW3hbGX3lHROaXMgaXMgeW91CIBmbGFnlHJhZGFye3Byb2dyYW1taW3nX2lZX2ltCG9ydGFUdF9nb29kX2pVYl9ICm9
```

Using an online base64 decoder i got this
```bash
HeRlo again , wou dida goUd joi`wowaTd HecauseyUu did a goodjU`and youcalfimyUuy`feg ilthe emoftext , goodecdamdUltfU
get to takea 
eYt and have agUod night beZauYe wou aregUod rUgrammeand doT't forgettUsubmit the feg and yeYye Iwant to make the baYe64ve
y loTg HecauseI waTt to Z
eate a Rot of hUtoYbecaue theezzwpeopRe fimletNis is youflagradar{programmim_iY_imortaTt_good_jUb_H
o
```

I noticed that the flag is at the end of the text, so i went through the base64 code and fixed it manually.

## Flag

radar{programmig_is_important_good_job_bro}
