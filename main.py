import requests
from bs4 import BeautifulSoup


url = 'https://music.apple.com/us/playlist/relax/pl.08b4e7005b29497db6578ebaece77a8d'

# Assign apple playlist as ap to request.get(url) for the playlist to scrape
ap = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

cls = soup.find_all('class')

print(cls)