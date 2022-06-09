import requests
from bs4 import BeautifulSoup
import os

count = 1
for filename in os.listdir(os.getcwd()):
	print(filename)
	dst = f"cartera-cuero-{str(count)}.jpg"
	src =f"{os.getcwd()}/{filename}"
	dst =f"{os.getcwd()}/{dst}"
	os.rename(src, dst)
	count+=1