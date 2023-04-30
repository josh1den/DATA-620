# Network And Sentiment Analysis of Pitchfork Album Reviews, 2018-2023

### Introduction

In this project, I will analyze data from 6000 Pitchfork reviews from 2018 to 2023. 

[Pitchfork](https://pitchfork.com/) is a highly influential, industry-leading online music publication producing original album reviews in addition to features, news articles, and more. Pitchfork's album review ratings system assigns a score from 0 to 10 based on internal polling. An album review score can have significant effect on artist's careers, affecting sales and marketing, live touring and festival opportunities, licensing placement and fees, digital streamining playlists and radio pickup, physical distribution orders, future partnership opportunities and terms, and more. Generally a rating score of 7.0 or above is considered good, while 8.0 or above is considered excellent. Conversely, a score below 6.5 is considered poor, while a score below 6.0 is considered bad.

Of particular interest is the phenomenon of good reviews and bad scores. 

I have acquired this [data](https://github.com/josh1den/DATA-620/tree/main/FINAL_PROJECT/data) by writing original python [scripts](https://github.com/josh1den/DATA-620/tree/main/FINAL_PROJECT/scripts) identifying the review pages and extracting the following data fields:

- **Artist**, *the artist name*
- **Album**, *the album being reviewed*
- **Genre**, *the genre of music*
- **Label**, *the record label releasing the album*
- **Release Year**, *the year the album is released*
- **Author**, *the writer of the review*
- **Published**, *publishing date of the review*
- **Best New Music**, *whether the review received Best New Music*
- **Best New Reissue**, *whether the review received Best New Reissue*
- **Score**, *album's ratings score*
- **Review**, *full text of the album review*
- **URL**, *link to the review*

### Proposed Analysis

This analysis will consist of three parts.

The **sentiment analysis** component will look at the quality of the review text and assign a score to each rating. 

The **network analysis** component will look to identify and visualize the relationship between writers and genre, writers and labels, and labels and genre. 

Finally, predictive models will be developed and deployed to determine which factors (label, genre, quality of text, writer centrality measures) if any are predictive of ratings score. 


