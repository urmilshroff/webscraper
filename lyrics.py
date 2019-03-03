import bs4
import requests
from halo import Halo

song_name = input("Enter name of the song:\n")
song_artist = input("Enter name of the artist:\n")

spinner = Halo(text="Fetching lyrics for '{}' by {}...".format(song_name, song_artist), spinner="dots")
spinner.start()

song_name = song_name.replace(" ", "-")
song_artist = song_artist.replace(" ", "-")
song_link = "https://genius.com/" + song_artist + "-" + song_name + "-lyrics"

res = requests.get(song_link)
soup = bs4.BeautifulSoup(res.text, "lxml")

lyrics = soup.select("p")

spinner.stop()

print("\n------------------------------------------------------------")
print("------------------------------------------------------------")
print("\n", lyrics[0].text)
print("\n------------------------------------------------------------")
print("------------------------------------------------------------")