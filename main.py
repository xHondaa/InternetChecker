import time
import urllib.request
from playsound import playsound

down = True
sec = 1
min = sec * 60
hour = sec * 3600

timeChosen = float(input("How often do you want me to check? (in seconds)\n"))

#Uncomment this if you want to change the method with which you choose the delay between each request

# timeChosen = int(input("How many hours do you want me to check?\n"))*hour + int(input("How many minutes?"))*min + int(input("How many seconds?\n"))*sec

#The URL requested to check with
url = "https://www.google.com"

while down:
    t = timeChosen
    try:
        x = urllib.request.urlopen(url).reason
        print(x)
        down = False
        playsound("a.mp3")
    except urllib.error.URLError:
        print("Still down")
        print("Checking again in " + str(timeChosen) + " seconds.")
        time.sleep(float(timeChosen))
#        print('mmm')
