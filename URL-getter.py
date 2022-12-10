from urllib.request import urlopen
import os
import requests
from clint.textui import progress

if os.name == 'nt': os.system('cls')
else: os.system('clear')

# Ask the user for the video URL
URL = input('\nPlease enter the URL of the dessired video:\n>> ')

# Localization of the image: Image URL
# 
# The first goal is to have the path of the image that is used as the thumbnail
# from a YouTube video. To do this, the first step is to obtain the source code of the
# of the video from which you want to obtain the thumbnail.

print('\nGetting the thumbnail URL...', end='')
page_source = str(urlopen(URL).read()) # Get the source-code

# The image can be found in the '<link rel="image_src" href=' block.
to_find = '<link rel="image_src" href='

index = page_source.find(to_find) # Get the index of the 'to_find' start 
URL = page_source[index + len(to_find) + 1 :] # Cut & delete until the start of the image URL

index = URL.find('\"') # Get the index of the next char to the image URL ' " '  
URL = URL[:index] # Get the URL only
print("Done\n")

# Now we need to download the image, now that we have it's link:
print("Downloading the thumbnail image...")
request = requests.get(URL, stream=True)

with open('thumbnail.jpg', 'wb') as f:
    total_length = int(request.headers.get('content-length'))
    for chunk in progress.bar(request.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
        if chunk:
            f.write(chunk)
            f.flush()

print("")