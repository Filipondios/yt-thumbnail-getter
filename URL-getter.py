from urllib.request import urlopen
import os

if os.name == 'nt': os.system('cls')
else: os.system('clear')

''' Ask the user for the video URL '''
URL = input('\nPlease enter the URL of the dessired video:\n>> ')

'''
Localization of the image: Image URL
 
The first goal is to have the path of the image that is used as the thumbnail
from a YouTube video. To do this, the first step is to obtain the source code of the
of the video from which you want to obtain the thumbnail.
'''
page_source = str(urlopen(URL).read()) # Get the source-code

''' 
The next step is dowloading that image. 

There are some types of thumbnails that can be found in the source code:
    -   480x360px
    -   1280x720px
Those are the available images in the source code, in order if you search ".jpg".
We need to ask the user what image wants to download.
'''
option = None

while(option == None):
    print('''\nThere are two different resolutions for the image. Choose one (the input must be the number):
    (0) 480x360px
    (1) 1280x720px''')
    option = int(input(">> "))

    if option != 0 and option != 1:
        option = None

if option == 0: # 480x360px
    print('The user selected 480x360px')
    # More stuff todo

else: # 1280x720px
    print('The user selected 1280x720px')
    # More stuff todo

# Muchhh more stuff todo...