#voice assistant code
import pyttsx3 #text to speech
import speech_recognition as sr 
import datetime
import pyautogui
import speedtest
import requests
from bs4 import BeautifulSoup
import datetime
import os
import platform
import subprocess
import pyjokes
import sqlite3
#from dbcreate import addlog

#  voice settings
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)


#  initializing the speech recognizer
r= sr.Recognizer()

#  sage speaks with this function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

platform= platform.system()

#  taking spoken words from microphone as input
def command_me():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5) #to recognize threshold noise level
        print("Listening...")
        audio1=r.listen(source) #get input from user

        MyQuery=r.recognize_google(audio1, language='en-in') #using google to recognize audio
        MyQuery=MyQuery.lower()
        print("You said- "+MyQuery)
        #speak(MyQuery)
        return MyQuery

        

#  greetings of the day
def greetings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!\n")
        speak("Good Morning")
    elif hour>=12 and hour<16:
        print("Good Afternoon!\n")
        speak("Good Afternoon")
    else:
        print("Good Evening!\n")
        speak("Good Evening!")
    speak("Please tell me, how can I help you?")




#  main function
if __name__ == "__main__":
    while True:
        MyQuery=command_me().lower()

        #  conversation
        if "hello sage" in MyQuery:
            greetings()
            from dbcreate import addlog
            addlog(MyQuery)
        elif "who are you" in MyQuery:
            speak("i am sage ")
            from dbcreate import addlog
            addlog(MyQuery)
        elif 'hello' in MyQuery:
            speak("Hello , how are you?")
            from dbcreate import addlog
            addlog(MyQuery)
        elif "i am fine" in MyQuery:
            speak("That's good to hear ")
            from dbcreate import addlog
            addlog(MyQuery)
        elif 'how are you' in MyQuery:
            speak("i am doing great ")
            from dbcreate import addlog
            addlog(MyQuery)
        elif "i am not fine" in MyQuery:
            speak("Don't worry , i am here with you , you can tell me anything")
            from dbcreate import addlog
            addlog(MyQuery)
        elif "thank you" in MyQuery:
            speak("you're welcome")
            from dbcreate import addlog
            addlog(MyQuery)
        elif "where do you live" in MyQuery:
            speak("My address is in your computer")
            from dbcreate import addlog
            addlog(MyQuery)
        elif "operating system" in MyQuery:
            speak("Your operating system is"+ platform)
            print(platform)
            from dbcreate import addlog
            addlog(MyQuery)
        elif "bye" in MyQuery:
            speak("Until next time")
            from dbcreate import addlog
            addlog(MyQuery)
            exit()


        # see logs
        elif "complete activity" in MyQuery:
            speak("here is your activity log")
            conn = sqlite3.connect('Sage.db')
            cursor = conn.execute("SELECT * FROM ActivityLogs ORDER BY QueryNo DESC") 
            for row in cursor:
                print(row)
            conn.close()
            from dbcreate import addlog
            addlog(MyQuery)
        
        elif "recent activity" in MyQuery:
            speak("here is your activity log")
            conn = sqlite3.connect('Sage.db')
            cursor = conn.execute("SELECT * FROM ActivityLogs ORDER BY QueryNo DESC LIMIT 5") 
            for row in cursor:
                print(row)
            conn.close()
            from dbcreate import addlog
            addlog(MyQuery)



        #  news
        elif "today's news" in MyQuery:
            from getNews import todays_news
            todays_news()
            from dbcreate import addlog
            addlog(MyQuery)
        elif "today's latest news" in MyQuery:
            from getNews import todays_news
            todays_news()
            from dbcreate import addlog
            addlog(MyQuery)
        elif "latest news" in MyQuery:
            from getNews import todays_news
            todays_news()
            from dbcreate import addlog
            addlog(MyQuery)

        #open any installed app 
        elif "launch" in MyQuery:
            if(platform=="Windows"):
                try:
                    from dbcreate import addlog
                    addlog(MyQuery)
                    MyQuery = MyQuery.replace('open' , '')
                    MyQuery = MyQuery.replace('sage' , '')
                    MyQuery = MyQuery.replace('launch' , '')
                    pyautogui.press('super')
                    pyautogui.typewrite(MyQuery)
                    pyautogui.press("enter")
                except:
                    speak("sorry, i can't open this application right now.")
            else:
                try:
                    from dbcreate import addlog
                    addlog(MyQuery)
                    MyQuery = MyQuery.replace('open' , '')
                    MyQuery = MyQuery.replace('sage' , '')
                    MyQuery = MyQuery.replace('launch' , '')
                    app_path = "/Applications/{}.app".format(MyQuery)
                    subprocess.call(["open", "-a", app_path])
                except:
                    speak("sorry, i can't open this application right now.")



        #  browsing 
        elif "google" in MyQuery:
            from searchNow import searchGoogle
            searchGoogle(MyQuery)
            from dbcreate import addlog
            addlog(MyQuery)

        elif "youtube" in MyQuery:
            from searchNow import searchYoutube
            searchYoutube(MyQuery)
            from dbcreate import addlog
            addlog(MyQuery)

        elif "wikipedia" in MyQuery:
            from searchNow import searchWikipedia
            searchWikipedia(MyQuery)
            from dbcreate import addlog
            addlog(MyQuery)
        
        #  for media controls 
        elif "pause video" in MyQuery:
            pyautogui.press("k")
            speak("video is now paused")
            from dbcreate import addlog
            addlog(MyQuery)
        elif "play video" in MyQuery:
            pyautogui.press("k")
            speak("video played")
            from dbcreate import addlog
            addlog(MyQuery)
        elif "mute video" in MyQuery:
            pyautogui.press("m")
            speak("video is now  muted")
            from dbcreate import addlog
            addlog(MyQuery)

        elif "volume up" in MyQuery:
            from keyboard import volumeup
            volumeup()
            from dbcreate import addlog
            addlog(MyQuery)
        elif "full volume" in MyQuery:
            from keyboard import fullvolume
            fullvolume()
            from dbcreate import addlog
            addlog(MyQuery)
        elif "volume down" in MyQuery:
            from keyboard import volumedown
            volumedown()
            from dbcreate import addlog
            addlog(MyQuery)
                
        elif "forward video" in MyQuery:
            from keyboard import forward
            forward()
            from dbcreate import addlog
            addlog(MyQuery)
        elif "backward video" in MyQuery:
            from keyboard import backward
            backward()
            from dbcreate import addlog
            addlog(MyQuery)

        #camera and screenshots   
        elif "take screenshot" in MyQuery:
            image = pyautogui.screenshot()
            image.save("Screenshot.png")
            print("Screenshot is captured and saved.")
            speak("screenshot is captured and saved")
            from dbcreate import addlog
            addlog(MyQuery)

        elif "click my photo" in MyQuery:
            pyautogui.press("super") #windows key
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(3)
            speak("smile")
            pyautogui.press("enter")
            print("photo captured")
            speak("Photo captured.")
            from dbcreate import addlog
            addlog(MyQuery)
              
        # temperature & weather inforamtion
        elif "temperature" in MyQuery:
                    search = "temperature in nagpur"
                    url = f"https://www.google.com/search?q={search}"
                    req = requests.get(url)
                    data = BeautifulSoup(req.text , "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"Current {search} is {temp}")
                    speak(f"Current {search} is {temp}")
                    from dbcreate import addlog
                    addlog(MyQuery)
                
        elif "weather" in MyQuery:
                    search = "weather in nagpur"
                    url = f"https://www.google.com/search?q={search}"
                    req = requests.get(url)
                    data = BeautifulSoup(req.text , "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"Current {search} is {temp}")
                    speak(f"Current {search} is {temp}")
                    from dbcreate import addlog
                    addlog(MyQuery)

        #joke
        elif "tell me a joke" in MyQuery:
            joke=pyjokes.get_joke(language="en", category="all")
            print("Joke: ",joke)
            speak(joke)
            from dbcreate import addlog
            addlog(MyQuery)


        #time and date info
        elif "the time" in MyQuery:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Current time is",time)
            speak(f"Current time is {time}")
            from dbcreate import addlog
            addlog(MyQuery)

        #internet speed
        elif "internet speed" in MyQuery:
            speed_test = speedtest.Speedtest()
            download_speed = round(speed_test.download()/1048576) #by default it is in bytes so we divide it by 1024*1024= 1048576
            print("Your download speed is", download_speed,"mbps.") 
            speak("your download speed in mbps is ")
            speak(download_speed)
            upload_speed = round(speed_test.upload()/1048576)
            print("Your upload speed is", upload_speed,"mbps.")
            speak("your upload speed in mbps is ")
            speak(upload_speed)
            from dbcreate import addlog
            addlog(MyQuery)

        # shutdown & restart
        elif "shut down my system" in MyQuery or "shutdown my system" in MyQuery:
            speak("Are you sure you want to shutdown your system")
            print("Say YES or NO")
            shutdown=command_me().lower()
            if "yes" in shutdown:
                speak("Now, shutting down the system, have a nice day")
                from dbcreate import addlog
                addlog(MyQuery)
                os.system("shutdown /s /t 1") #/s= seconds /t= time interval 1 is duration
            elif "no" in shutdown:
                break

        elif "restart my system" in MyQuery:
            speak("Are you sure you want to restart your system")
            print("Say YES or NO")
            restart=command_me().lower()
            if "yes" in restart:
                speak("Now, restarting the system, have a nice day")
                from dbcreate import addlog
                addlog(MyQuery)
                os.system("shutdown /r /t 1") #y=yes f=force
            elif "no" in restart:
                break

