import requests
from datetime import date
import time
# we import the Twilio client from the dependency we just installed
import telegram_send
telegram_send.send(messages=["Wow that was easy!"])

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number


url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
params={
    "pincode":500010,
    "date" : date.today().strftime("%d-%m-%Y")

}


while True:
    res= requests.get(url=url,params=params)
    print("request sent")
    data= res.json()

    for i in data["centers"]:
        for j in i["sessions"]:
            if j['min_age_limit']==18 and j['vaccine']=='COVISHIELD' and j['available_capacity']>0 and j['available_capacity_dose1']>0:
                print(j)

    time.sleep(5)