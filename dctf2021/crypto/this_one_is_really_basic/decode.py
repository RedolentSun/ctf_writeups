import base64

data = open("cipher.txt", "r").read()
decoded = base64.b64decode(data)

for i in range(41):
    print(i)
    decoded = base64.b64decode(decoded)

print(decoded)