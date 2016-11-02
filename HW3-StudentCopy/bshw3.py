# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import urllib.request, urllib.parse, urllib.error
import re
import requests
import unicodedata
from bs4 import BeautifulSoup

# import HTMLParser
# h = HTMLParser.HTMLParser()
# h.unescape('&lt; &gt;')

url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

find_student = soup.find_all(text = re.compile('student'))
for student in find_student:
	AMAZING_student = str(student).replace('student', 'AMAZING student')
	student.replace_with(AMAZING_student)

img_tags = soup('img')
for img in img_tags:
	local_img = img.replace_with('<img src ="file:///Users/AditiRajadhyaksha/Desktop/project3/HW3-StudentCopy/media/logo.png"/>')

# # Replace '&lt;' with '<'
# find_error = soup.find_all(text = re.compile('&lt;'))
# for error in find_error:
# 	fixed_error = str(error).replace('&lt;', '<')
# 	error.replace_with(fixed_error)

# #&gt;
# find_other_error = soup.find_all(text = re.compile('&gt;'))
# for other_error in find_other_error:
# 	fixed_other_error = str(other_error).replace('&gt;', '>')
# 	other_error.replace_with(fixed_error)


print(soup.prettify(formatter=None))





#class for main image: class="ytp-thumbnail-overlay ytp-cued-thumbnail-overlay"