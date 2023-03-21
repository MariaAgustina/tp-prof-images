import requests
from bs4 import BeautifulSoup
import os
#https://unsplash.com/collections/2602638/cuero
#https://unsplash.com/collections/27931574/texture%2Fleather
#https://unsplash.com/collections/8586775/leather
#https://unsplash.com/collections/VeJcjl2BYyM/leather
#https://unsplash.com/collections/77620996/feminine-stories-in-leather
#https://unsplash.com/collections/47233760/leather
#https://unsplash.com/collections/ASemqymipZA/leather-girl
#https://unsplash.com/collections/_yp2nCWkY28/amati-mango-leather-
#https://unsplash.com/collections/831786/leather-jackets
#https://unsplash.com/collections/9939520/leather-shoes

url = 'https://www.instagram.com/explore/tags/cuero/'
folder_name = 'cuero-ig'

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

count = 1
for image in images:
	try:
		print(image)
		link = image['src']
		sep = '&'
		link = link.split(sep, 1)[0]
		name = "cuero-ig-" + str(count)
		with open(name.replace(' ','-').replace('/','') + '.jpg', 'wb') as f:
			im = requests.get(link)
			f.write(im.content)
			print('Writing ', name)
			count+=1
	except BaseException as error:
		print("Error scrapping image",error)
		


