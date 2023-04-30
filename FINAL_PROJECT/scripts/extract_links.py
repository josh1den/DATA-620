#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup  
import json
import time
from more_itertools import chunked

def extract_links():
    '''extracts first 500 pages of pitchfork review links'''

    # build list of review links
    reviews = []

    chunks = list(chunked(range(1,501), 20)) ## 500 pages in chunks of 20 pages

    # loop through pages
    for chunk in chunks:
        for c in chunk:
            url = "https://pitchfork.com/reviews/albums/?page=" + str(c)
            html = urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
        
            for tag in soup.find_all('a', class_="review__link"):
                links = tag.get('href')
                reviews.append(links)
            print("page {} complete...".format(c))
        print("moving to next chunk...")    
        time.sleep(15)
    
    time = get_ipython().run_line_magic('time', '')
    print("time elapsed: {}".format(time))
    return reviews

