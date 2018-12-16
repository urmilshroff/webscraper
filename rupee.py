import bs4
import requests
import operator

res=requests.get("http://dollarrupee.in/")
soup=bs4.BeautifulSoup(res.text,"lxml")

rate=soup.select(".item-page p strong")
rupee=float(rate[0].text)

print("Today's value: $1 = ₹{}".format(rupee))

dollar=int(input("Enter amount in USD:\n"))
print("Your conversion: ${} = ₹{}".format(dollar,round(dollar*rupee)))