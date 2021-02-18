import requests
import re

r = requests.get('https://www.google.com/')
exmp = re.search('(?<=title>).+?(?=</title>)',r.text,re.DOTALL).group().split()
print(exmp)