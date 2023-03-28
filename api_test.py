import requests

url = "http://localhost:5000/image"
image_path = "../VOC/validation/JPEGImages/im51.jpg"

with open(image_path, "rb") as f:
    response = requests.post(url, files={"images": f})
