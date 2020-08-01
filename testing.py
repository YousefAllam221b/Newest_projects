import re
text="yousef moataz01001097153 , asdf 01123810291,0"
mail= "YousefAllam221b@gmail.com"
number = re.compile("0\d{10}")
email=re.compile(r"(.*)(@.*)")
out=number.findall(text)
m=email.findall(mail)
print(m)
