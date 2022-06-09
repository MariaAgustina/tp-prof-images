import requests
from bs4 import BeautifulSoup
import os

for count,file in os.listdir(os.getcwd()):
	print(file)
	dst = f"cartera-cuero-{str(count)}.jpg"
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
    os.rename(src, dst)