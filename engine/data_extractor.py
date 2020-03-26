import requests

from bs4 import BeautifulSoup
from methods.extract_info import *


r = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(r.text, 'html.parser')

# Extract from HTML
ranks = soup.find_all('span', attrs={'class': 'rank'})
titles = soup.find_all('a', attrs={'class': 'storylink'})
subtext = soup("td", {'class': 'subtext'})

# Extract data from HTML lists
rank = extract_rank(ranks)
title = extract_title(titles)
score, comments = extract_score_comments(subtext)

# Merge results into a list of tuples
results = list(zip(rank, title, score, comments))

df = pd.DataFrame(results, columns=['Number of order', 'Title', 'Points', 'Amount of comments'])

