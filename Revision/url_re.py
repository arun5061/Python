import re,urllib.request
u=urllib.request.urlopen("http://www.rediff.com/")
text=u.read()
n=re.findall('<title>(.*)</title>',str(text))
print(n[0])

