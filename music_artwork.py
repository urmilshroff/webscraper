import bs4
import requests
import urllib.request

artist_name = input("Enter name of the artist: ")
print("Is it an album or a song?")
print("1. Album")
print("2. Song")
choice = int(input())

if choice is 1:
    album_name = input("Enter name of the album: ")
    album_name = album_name.replace(" ", "-")
    page_link = "https://genius.com/albums/" + artist_name + "/" + album_name

elif choice is 2:
    song_name = input("Enter name of the song: ")
    song_name = song_name.replace(" ", "-")
    page_link = "https://genius.com/" + artist_name + "-" + song_name + "-lyrics"

res = requests.get(page_link)
soup = bs4.BeautifulSoup(res.text, "lxml")

image = soup.select("img.cover_art-image")
img_url = image[0].get("src")

urllib.request.urlretrieve(img_url, "artwork.jpg")