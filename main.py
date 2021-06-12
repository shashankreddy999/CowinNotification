import time
import requests
import beepy
from datetime import date
from twilio.rest import Client


client = Client("AC31313e3579599d236102821a41cdfc20", "8fcef4fd1894de580134732fc4f98ca9")




url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"

#district id for hyderabad
params={
    "district_id":581,
    "date" : date.today().strftime("%d-%m-%Y")

}
#district id for medchal
params2={
    "district_id":596,
    "date" : date.today().strftime("%d-%m-%Y")

}

beepy.beep(5)
ind=0
while True:


    res= requests.get(url=url,params=params)
    res2=requests.get(url=url,params=params2)

    data= res.json()
    data2 = res.json()
    print("pinged ",ind)
    ind+=1
    for i in data["centers"]:
        for j in i["sessions"]:
            if j['min_age_limit']==18 and j['vaccine']=='COVISHIELD' and j['available_capacity']>0 and j['available_capacity_dose1']>0:
                client.messages.create(to="+919849965690",
                                       from_="+12107047917",
                                       body=i["name"]+"\n"+i['address']+"\n"+str(j['available_capacity'])+"\n"+j["date"])
                print("Vaccine Found")
                print(i["name"] + "\n" + i['address'] + "\n" + str(j['available_capacity']) + "\n" + j["date"])
                beepy.beep(5)

    for i in data2["centers"]:
        for j in i["sessions"]:
            if j['min_age_limit']==18 and j['vaccine']=='COVISHIELD' and j['available_capacity']>0 and j['available_capacity_dose1']>0:
                client.messages.create(to="+919849965690",
                                       from_="+12107047917",
                                       body=i["name"]+"\n"+i['address']+"\n"+str(j['available_capacity'])+"\n"+j["date"])
                print("Vaccine Found")
                print(i["name"]+"\n"+i['address']+"\n"+str(j['available_capacity'])+"\n"+j["date"])
                beepy.beep(5)
    time.sleep(3)