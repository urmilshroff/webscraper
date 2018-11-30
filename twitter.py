import bs4
import requests
import operator

user_id=input("Enter the username of the Twitter profile:\n")
user_link="https://twitter.com/"+user_id

res=requests.get(user_link)
soup=bs4.BeautifulSoup(res.text,"lxml")

name=soup.select(".ProfileHeaderCard-nameLink.u-textInheritColor.js-nav")

try:
    count=[]
    for item in soup.findAll("span",{"class":"ProfileNav-value"}):
        count.append(item.get("data-count"))
except IndexError:
    print("Error: missing or broken info!")

try:
    join=soup.select(".ProfileHeaderCard-joinDateText.js-tooltip.u-dir")
    joined=join[0].get("title")
except IndexError:
    print("Error: missing or broken info!")

try:
    print("\nSummary for Twitter user @{} (aka {}):".format(user_id,name[0].text))
except IndexError:
    print("Error: missing or broken info!")

try:
    print("\nNumber of Tweets: {}".format(count[0]))
    print("Number of following: {}".format(count[1]))
    print("Number of followers: {}".format(count[2]))
    print("Number of likes: {}".format(count[3]))
except IndexError:
    print("Error: missing or broken info!")

try:
    print("\nJoined Twitter at: {}".format(joined))
except IndexError:
    print("Error: missing or broken info!")