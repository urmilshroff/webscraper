import bs4
import requests

user_id=input("Enter the username of the GitHub profile:\n")
user_link="https://github.com/"+user_id

res=requests.get(user_link)
soup=bs4.BeautifulSoup(res.text,"lxml")

name=soup.select(".p-name.vcard-fullname.d-block.overflow-hidden")

print("Summary for GitHub user {} (aka {}):".format(user_id,name[0].text))