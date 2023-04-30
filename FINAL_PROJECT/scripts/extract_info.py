#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from urllib.request import urlopen
from bs4 import BeautifulSoup  
import json

def extract_info(soup):
    '''takes the soup object and extracts the data'''
    
    try:
        
        # extract url
        url = soup.head.find("meta", property="og:url").get("content")
    
        # extract ld-json data: header
        header = json.loads(soup.find('script', type='application/ld+json').string)

        review = header['reviewBody'].replace('&nbsp;', '').replace('\n', '').split('[#product:',1)[0]
        album = header['headline']
        author = header['author'][0]['name']
        published = header['datePublished'][:10]

        # extract javascript
        elements = soup.find('body', class_='standardnavigation-site-navigation logo-left-with-search-nav-variation').find('script', type="text/javascript")
        artist = elements.text.split('"headerProps":', 1)[1].split(',"uri"',1)[0].split('}}],',1)[1].replace('"','').split(':')[1]
        infoSlice = elements.text.split(',"infoSliceFields":',1)[1].split(',"lede":')[0] + "}"
        infoSlice_labels, infoSlice_ratings = infoSlice.split(',"isMusicReview"', 1)
        infoSlice_ratings = '{"isMusicReview"' + infoSlice_ratings
        labels = json.loads(infoSlice_labels)
        ratings = json.loads(infoSlice_ratings)

        # extract data from labels and ratings
        genre = labels['genre']
        label = labels['label']
        releaseYear = labels['releaseYear']

        bestNewMusic = ratings['musicRating']['isBestNewMusic']
        bestNewReissue = ratings['musicRating']['isBestNewReissue']
        score = ratings['musicRating']['score']
        
        return artist, album, genre, label, releaseYear, author, published, bestNewMusic, bestNewReissue, score, review, url
        
    except KeyError:
        
        url = soup.head.find("meta", property="og:url").get("content")
        artist = 'NA'
        album = 'NA'
        genre = 'NA'
        label = 'NA'
        releaseYear = 'NA'
        author = 'NA'
        published = 'NA'
        bestNewMusic = 'NA'
        bestNewReissue = 'NA'
        score = 'NA'
        review = 'NA'
        
        return artist, album, genre, label, releaseYear, author, published, bestNewMusic, bestNewReissue, score, review, url
        
    except IndexError:
        
        # extract url
        url = soup.head.find("meta", property="og:url").get("content")
    
        # extract ld-json data: header
        header = json.loads(soup.find('script', type='application/ld+json').string)

        review = header['reviewBody'].replace('&nbsp;', '').replace('\n', '').split('[#product:',1)[0]
        album = header['headline']
        author = header['author'][0]['name']
        published = header['datePublished'][:10]

        # extract javascript
        elements = soup.find('body', class_='standardnavigation-site-navigation logo-left-with-search-nav-variation').find('script', type="text/javascript")
        artist = 'Various Artists'
        infoSlice = elements.text.split(',"infoSliceFields":',1)[1].split(',"lede":')[0] + "}"
        infoSlice_labels, infoSlice_ratings = infoSlice.split(',"isMusicReview"', 1)
        infoSlice_ratings = '{"isMusicReview"' + infoSlice_ratings
        labels = json.loads(infoSlice_labels)
        ratings = json.loads(infoSlice_ratings)

        # extract data from labels and ratings
        genre = labels['genre']
        label = labels['label']
        releaseYear = labels['releaseYear']

        bestNewMusic = ratings['musicRating']['isBestNewMusic']
        bestNewReissue = ratings['musicRating']['isBestNewReissue']
        score = ratings['musicRating']['score']
        
        return artist, album, genre, label, releaseYear, author, published, bestNewMusic, bestNewReissue, score, review, url

    except (json.JSONDecodeError):
        
        # extract url
        url = soup.head.find("meta", property="og:url").get("content")
    
        # extract ld-json data: header
        header = json.loads(soup.find('script', type='application/ld+json').string)

        review = header['reviewBody'].replace('&nbsp;', '').replace('\n', '').split('[#product:',1)[0]
        album = header['headline']
        author = header['author'][0]['name']
        published = header['datePublished'][:10]

        # extract javascript
        elements = soup.find('body', class_='standardnavigation-site-navigation logo-left-with-search-nav-variation').find('script', type="text/javascript")
        artist = elements.text.split('"headerProps":', 1)[1].split(',"uri"',1)[0].split('}}],',1)[1].replace('"','').split(':')[1]
        infoSlice = elements.text.split(',"infoSliceFields":',1)[1].split(',"lede":')[0] + "}"
        infoSlice_labels, infoSlice_ratings = infoSlice.split(',"isMusicReview"', 1)
        infoSlice_ratings = '{"isMusicReview"' + infoSlice_ratings
        labels = json.loads(infoSlice_labels)
        ratings = json.loads(infoSlice_ratings.split(',"modifiedDate":',1)[0] + "}")

        # extract data from labels and ratings
        genre = labels['genre']
        label = labels['label']
        releaseYear = labels['releaseYear']

        bestNewMusic = ratings['musicRating']['isBestNewMusic']
        bestNewReissue = ratings['musicRating']['isBestNewReissue']
        score = ratings['musicRating']['score']
        
        return artist, album, genre, label, releaseYear, author, published, bestNewMusic, bestNewReissue, score, review, url

