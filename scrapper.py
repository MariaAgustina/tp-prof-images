import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.olx.com.ar'
folder_name = 'test'

try:
	os.mkdir(os.path.join(os.getcwd(), folder_name))
except:
	"Error creating directory"
	pass
	
os.chdir(os.path.join(os.getcwd(), folder_name))
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')

for image in images:
	link = image['src']
	name = image['alt']
	with open(name.replace(' ','-').replace('/','') + '.jpg', 'wb') as f:
		im = requests.get(link)
		f.write(im.content)
		print('Writing ', name)
