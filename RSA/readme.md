# RSA

Show me your skills in RSA :P

## Walkthrough

The first thing I did was factoring n using factordb.

p=2045145391
q=3704852779

Then I wrote a simple script to retrive the clear message from all the ciphered texts

```python
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
```
Every ciphered text gave a 6 digits number. That's why i used a,b and c in the script to extract every 2 digits and decode them using chr().

The output of the script was 

```bash
GEYTIIBZG4QDCMBQEA4TOIBRGE2CAMJSGMQDCMBSEA4TOIBZHEQDCMJWEAYTCMJAGEYTIIBUHEQDCMJQEAYTAMZAHE2SAOJZEA3DIIBRGEYCAOJVEA4TSIBRGE2CANRUEA4TSIBRGA3SAOJVEAYTCNBAGEYTKIBZG4QDCMRV
```
It is base32.
I used an online base32 decoder and i got this 

```bash
114 97 100 97 114 123 102 97 99 116 111 114 49 110 103 95 99 64 110 95 99 114 64 99 107 95 114 115 97 125
```

So i used a Decimal to ascii converter online.

## Flag
radar{factor1ng_c@n_cr@ck_rsa}
