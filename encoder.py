import base64

text = open('ServerForEecode.txt','r')
# print(text.read())
sample_string_bytes = text.read().encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
# print(base64_string)
with open('SS','w') as f:
    f.write(base64_string)