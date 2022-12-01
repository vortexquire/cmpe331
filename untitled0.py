# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MdDINfEKamf0A1BgoOF0mQ8bOFM1jo_Q
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select('td.titleColumn')
ratings = [b.attrs.get('data-value')
		for b in soup.select('td.posterColumn span[name=ir]')]

a = []

for index in range(0, len(movies)):
	movie_string = movies[index].get_text()
	movie = (' '.join(movie_string.split()).replace('.', ''))
	movie_title = movie[len(str(index))+1:-7]
	year = re.search('\((.*?)\)', movie_string).group(1)
	place = movie[:len(str(index))-(len(movie))]
	data = {"place": place,
			"movie_title": movie_title,
			"rating": ratings[index],
			}
	a.append(data)

for movie in a:
	print(movie['place'], movie['movie_title'], movie['rating'])

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
		for b in soup.select('td.posterColumn span[name=ir]')]




# create a empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
	
	# Separating movie into: 'place',
	# 'title', 'year'
	movie_string = movies[index].get_text()
	movie = (' '.join(movie_string.split()).replace('.', ''))
	movie_title = movie[len(str(index))+1:-7]
	year = re.search('\((.*?)\)', movie_string).group(1)
	place = movie[:len(str(index))-(len(movie))]
	data = {"place": place,
			"movie_title": movie_title,
			"rating": ratings[index],
			"year": year,
			"star_cast": crew[index],
			}
	list.append(data)

# printing movie details with its rating.
for movie in list:
	print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
		') -', 'Starring:', movie['star_cast'], movie['rating'])


##.......##
df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv',index=False)