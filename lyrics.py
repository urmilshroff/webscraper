import bs4
import requests

song_name=input("Enter name of the song:\n")
song_artist=input("Enter name of the artist:\n")

print("\nFetching lyrics for '{}' by {}...".format(song_name,song_artist))

song_name=song_name.replace(" ","-")
song_artist=song_artist.replace(" ","-")
song_link="https://genius.com/"+song_artist+"-"+song_name+"-lyrics"

res=requests.get(song_link)
soup=bs4.BeautifulSoup(res.text,"lxml")

lyrics=soup.select("p")
print("\n------------------------------------------------------------")
print("------------------------------------------------------------")
print("\n",lyrics[0].text)
print("\n------------------------------------------------------------")
print("------------------------------------------------------------")