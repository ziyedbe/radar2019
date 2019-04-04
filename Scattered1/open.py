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
