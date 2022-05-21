import requests
from bs4 import BeautifulSoup
import os
import cv2

url = 'https://bolsos.mercadolibre.com.ar/carteras-billeteras/cartera-gamuza#D%5BA:cartera%20gamuza,on%5D'
folder_name = 'cartera-gamuza'

os.chdir(os.path.join(os.getcwd(), folder_name))
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img',{"class": "ui-search-result-image__element"})

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
		
print(os.listdir(os.getcwd()))
for file in os.listdir(os.getcwd()):
	print(file)
	try:
		img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
		h, w = img.shape
		if(not (h > 100 or w > 100)):
			os.remove(file)
	except:
		print("Error getting image size")