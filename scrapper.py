import requests
from bs4 import BeautifulSoup
import os

url = 'https://images.search.yahoo.com/search/images;_ylt=AwrFciwv7MJjgW42l1aJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRmcgNzZnAEZnIyA3A6cyx2OmksbTpzYi10b3AEZ3ByaWQDb0ZzNDlMOVVRTC5nSG5CUFduN1R2QQRuX3JzbHQDMARuX3N1Z2cDMTAEb3JpZ2luA2ltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAM2BHF1ZXJ5A2dhbXV6YQR0X3N0bXADMTY3MzcxODg5Ng--?p=gamuza&fr=sfp&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&ei=UTF-8&x=wrt'
folder_name = 'material-gamuza'

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

count = 467
for image in images:
	try:
		print(image)
		link = image['src']
		sep = '&'
		link = link.split(sep, 1)[0]
		name = "gamuza" + str(count)
		with open(name.replace(' ','-').replace('/','') + '.jpg', 'wb') as f:
			im = requests.get(link)
			f.write(im.content)
			print('Writing ', name)
			count+=1
	except BaseException as error:
		print("Error scrapping image",error)
		


