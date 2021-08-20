import base64

IMAGE = 'src\github_heart.png'

with open(IMAGE, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())

print(encoded_string)
