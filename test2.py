import requests, uuid

api_key = 'acc_3f798630dd003f8'
api_secret = '9e0720e58140cf49ce4a1494482ca516'
image_url = 'https://images.pexels.com/photos/733416/pexels-photo-733416.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
image_path = 'H:\Semester3\PROG23372\Assignment2\Images\Image.jpeg'



# response = requests.get(
#     'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
#     auth=(api_key, api_secret))

response = requests.get(image_url)

if response.status_code:
    filepath = open(f"image_{uuid.uuid4()}.png", 'wb')
    filepath.write(response.content)
    filepath.close()

def save_Image(image_url):
    response = requests.get(image_url)
    pass

# pretty_list = response.json()["result"]["tags"]

# for index in range(len(pretty_list)):
#     print(pretty_list[index])