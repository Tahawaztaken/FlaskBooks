import requests


#image_url = 'https://imagga.com/static/images/tagging/wind-farm-538576_640.jpg'
image_path = 'H:\Semester3\PROG23372\Assignment2\Images\circle.png'



"UPLOADING IMAGES"
def upload_Image(image_Path):
    response = requests.post(
        'https://api.imagga.com/v2/uploads',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    return response.json()["result"]["upload_id"]


response = requests.get(
    'https://api.imagga.com/v2/tags?image_upload_id=%s' % upload_Image(image_path),
    auth=(api_key, api_secret))


pretty_list = response.json()["result"]["tags"]

tag_list = []

for index in range(len(pretty_list)):
    tag_list.append({'tag': pretty_list[index]['tag']['en'], 'confidence': pretty_list[index]['confidence'] })

print(tag_list)


