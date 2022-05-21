import requests
from bs4 import BeautifulSoup
import os

url = 'https://listado.mercadolibre.com.ar/cartera-cuero#D%5BA:cartera%20cuero%5D'
folder_name = 'cartera-cuero'

print("URL A DESCARGAR: ", url)

try:
	os.mkdir(os.path.join(os.getcwd(), folder_name))
except:
	"Error creating directory"
	pass

os.chdir(os.path.join(os.getcwd(), folder_name))
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')

print(images)

for image in images:
	try:
		link = image['data-src']
		name = image['alt']
		with open(name.replace(' ','-').replace('/','') + '.jpg', 'wb') as f:
			im = requests.get(link)
			f.write(im.content)
			print('Writing ', name)
	except BaseException as error:
		print("Error scrapping image",error)
		

