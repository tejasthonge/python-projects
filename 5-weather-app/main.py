import requests  #by using theis we can accasse the data from the network
import json #for the pars the url
import pyttsx3 #for in speach formate not in text 

#search on google weather api free


city = input("Enter the city :")
url =f"https://api.weatherapi.com/v1/current.json?key=50b51e26c4b34b6a8a3203512241401&q={city}"

r = requests.get(url)
print(r.text)  #it print all the data of wethor in url in json formate we can comment this if we not requre
wdic = json.loads(r.text)
data = wdic["current"]["temp_c"]

speaker =pyttsx3.init()
speaker.say(f"the current weather in {city} as follow : tempreture is {data}")
speaker.runAndWait()