import requests
from bs4 import BeautifulSoup
import os
import cv2

url = 'https://bolsos.mercadolibre.com.ar/carteras-billeteras/cartera-lana_PriceRange_4500-0_NoIndex_True#applied_filter_id%3Dprice%26applied_filter_name%3DPrecio%26applied_filter_order%3D4%26applied_value_id%3D4500.0-*%26applied_value_name%3DMás+de+%244.500%26applied_value_order%3D3%26applied_value_results%3D32%26is_custom%3Dfalse'
folder_name = 'cartera-lana'

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