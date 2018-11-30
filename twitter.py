import bs4
import requests
import operator

user_id=input("Enter the username of the Twitter profile:\n")
user_link="https://twitter.com/"+user_id

res=requests.get(user_link)
soup=bs4.BeautifulSoup(res.text,"lxml")

name=soup.select(".ProfileHeaderCard-nameLink.u-textInheritColor.js-nav")

count=[]
for item in soup.findAll("span",{"class":"ProfileNav-value"}):
    count.append(item.get("data-count"))

join=soup.select(".ProfileHeaderCard-joinDateText.js-tooltip.u-dir")
joined=join[0].get("title")

print("\nSummary for Twitter user @{} (aka {}):".format(user_id,name[0].text))

print("\nNumber of Tweets: {}".format(count[0]))
print("Number of following: {}".format(count[1]))
print("Number of followers: {}".format(count[2]))
print("Number of likes: {}".format(count[3]))

print("\nJoined Twitter at: {}".format(joined))