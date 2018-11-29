import bs4
import requests

user_id=input("Enter the username of the GitHub profile:\n")
user_link="https://github.com/"+user_id

res=requests.get(user_link)
soup=bs4.BeautifulSoup(res.text,"lxml")

name=soup.select(".p-name.vcard-fullname.d-block.overflow-hidden")
count=soup.select(".Counter")

print("Summary for GitHub user {} (aka {}):".format(user_id,name[0].text))
print("Number of repositories: {}".format(count[0].text.strip()))
print("Number of stars: {}".format(count[1].text.strip()))
print("Number of followers: {}".format(count[2].text.strip()))
print("Number of following: {}".format(count[3].text.strip()))