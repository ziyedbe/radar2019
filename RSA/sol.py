n=7576962585305391589
p=2045145391
q=3704852779
ph= (p-1)*(q-1)
e=65537
d=4406608918927534373
f=open("cipher.txt","r")
content=f.readlines()
msg=""
for i in content:
    ch=""
    m=pow(int(i),d,n)
    a=m/10000
    b=(m-a*10000)/100
    c=(m-a*10000-b*100)
    ch = chr(a)+chr(b)+chr(c)
    msg+=ch
print(msg)
