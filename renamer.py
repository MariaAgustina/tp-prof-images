import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

count=1
folder="cueros-pinterest"
for filename in os.listdir(os.getcwd()):
    print(filename)
    dst = f"cuero-pinteret{str(count)}.jpg"
    src =f"{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{dst}"
    os.rename(src, dst)
    count+=1

def resize_by_percentage(image, outfile, percentage):
    with Image.open (image) as im:
        width, height = im.size
        resized_dimensions = (int(width * percentage), int(height * percentage))
        resized = im.resize(resized_dimensions)
        resized.save(outfile)

#for file in os.listdir(os.getcwd()):
 #   if not "renamer" in file and os.path.getsize(file) > 150000:
  #      print(file)
   #     print(os.path.getsize(file))
    #    resize_by_percentage(file, file, 0.5)