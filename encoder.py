import base64, os
from time import gmtime, strftime

text = open('ServerForEecode.txt','r')
# print(text.read())
sample_string_bytes = text.read().encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
# print(base64_string)
with open('SS','w') as f:
    f.write(base64_string)

os.system(f'git commit -am \"Latest Update: {strftime("%Y-%m-%d %H%M%S %z", gmtime())}\"')
os.system('git push origin main')