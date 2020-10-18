import requests
url = "https://wikipedia.org/wiki/File:Taj_Mahal_(Edited).jpeg"
filename = url.split(':')[-1]
response = requests.get(url)
content = response.content
with open(filename + '.html', 'wb') as f:
    f.write(content)

