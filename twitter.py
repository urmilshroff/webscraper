import bs4
import requests
import operator

user_id=input("Enter the username of the Twitter profile:\n")
user_link="https://twitter.com/"+user_id

res=requests.get(user_link)
soup=bs4.BeautifulSoup(res.text,"lxml")

name=soup.select(".ProfileHeaderCard-nameLink.u-textInheritColor.js-nav")

print("\nSummary for Twitter user {} (aka {}):".format(user_id,name[0].text))