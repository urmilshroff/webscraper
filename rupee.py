import bs4
import requests
import operator

res=requests.get("http://dollarrupee.in/")
soup=bs4.BeautifulSoup(res.text,"lxml")

rate=soup.select(".item-page p strong")
rupee=float(rate[0].text)

print("Today's rate: $1 = ₹{}".format(rupee))

choice=int(input("What do you want to convert?\n1. Dollars to Rupees\n2. Rupees to Dollars\n"))

if(choice==1):
    amount=int(input("Enter amount in USD:\n"))
    print("Today's conversion: ${} = ₹{} (approx.)".format(amount,round(amount*rupee)))
    
if(choice==2):
    amount=int(input("Enter amount in INR:\n"))
    print("Today's conversion: ₹{} = ${} (approx.)".format(amount,round(amount/rupee)))
    
else:
    print("Bad choice!")