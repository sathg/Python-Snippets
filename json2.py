import json
from urllib.request import urlopen
import ssl

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_314862.json"
html = urlopen(url, context=ctx).read()

info = json.loads(html)
print('User count:', len(info))
print(info['comments'])

counting = 0
for item in info['comments']:
    counting = counting + int(item['count'])

print(counting)
