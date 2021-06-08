import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver

reg = ''
# Apple music URL for the playlist
url = 'https://music.apple.com/us/playlist/relax/pl.08b4e7005b29497db6578ebaece77a8d'

# Assign apple playlist as ap to request.get(url) for the playlist to scrape
ap = requests.get(url)

title = []
soup = BeautifulSoup(ap.content, 'html.parser')
asplit = []
artist = []
links = []
song_artist = []

# Time to wait for the pages to load (pl) and commands to be clicked/entered (cl). 
# Can be adjusted based on internet/computer speed.
pl = 10
cl = 3

for link in soup.find_all('a'):
    links.append(link.get('href'))

for item in links:
    if item.startswith('https:'):
        asplit = item.split('/')
        artist.append(asplit[-2])

for cls in soup.find_all("div", class_="songs-list-row__song-name"):
    title.append(cls.text)

song_artist = [i + ' ,' + j for i, j in zip(title, artist)]

driver = webdriver.Chrome(
    'C:\Program Files\Google\chromedriver.exe'
)  # Optional argument, if not specified will search path.

driver.get('https://music.amazon.com/');
time.sleep(pl)  # Amazon site can take a bit to load.

# Must select signin since chromedriver won't have login cookies.
elem_signIn = driver.find_element_by_id('signInButton')
elem_signIn.click()

# Input login name/email
elem_email = driver.find_element_by_id("ap_email")
time.sleep(cl)  # Let the user actually see something!


elem_email.send_keys('LOGIN')

elem_pass = driver.find_element_by_id("ap_password")
time.sleep(cl)  # Let the user actually see something!

# Input login password
elem_pass.send_keys('PASSWORD')

elem_submit = driver.find_element_by_id("signInSubmit")
elem_submit.click()
time.sleep(pl)  

# Loop through and add the songs from the list of song titles.
for songs in title:
    # commmon failure spot if wait times are not long enough, may need to adjust (pl)
    # searches for the song in playlist in Amazon searchbar
    sel_song = driver.find_element_by_id("navbarSearchInput")
    time.sleep(cl) 

    sel_song.send_keys(songs)
    sel_song.submit()
    time.sleep(cl)  
    #song_select = driver.find_element_by_id('searchSuggestion1')
    #song_select.click()

    time.sleep(pl)  # Can adjust time as needed

    # These next steps choose your playlist to load the song too.
    # Currently this will only work for the top listed playlist on the page.
    click_option = driver.find_element_by_id('ic_action_more-a')
    click_option.click()
    time.sleep(3)
    opt_playlist = driver.find_element_by_id('label')
    opt_playlist.click()
    time.sleep(3)
    click_playlist = driver.find_element_by_class_name('button music-t1')
    click_playlist.click()
    time.sleep(3)
    search_box.submit()

    time.sleep(5)  # Let the user actually see something!

