import pyttsx3 #text to speech
import speech_recognition as sr 
import datetime
import pyautogui
import speedtest
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyjokes


#  voice settings by ishita
engine = pyttsx3.init('sapi5') #microsoft speech API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)


#  initializing the speech recognizer
r= sr.Recognizer()

#  sage speaks with this function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#  taking spoken words from microphone as input
def command_me():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5) #to recognize threshold noise level--pehele 0.2 tha
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
        elif "who are you" in MyQuery:
            speak("i am sage ")
        elif 'hello' in MyQuery:
            speak("Hello , how are you?")
        elif "i am fine" in MyQuery:
            speak("That's good to hear ")
        elif 'how are you' in MyQuery:
            speak("i am doing great ")
        elif "i am not fine" in MyQuery:
            speak("Don't worry , i am here with you , you can tell me anything")
        elif "thank you" in MyQuery:
            speak("you're welcome")
        elif "where do you live" in MyQuery:
            speak("My address is in your computer")
        elif "bye" in MyQuery:
            speak("Until next time")
            exit()

        #  news
        elif "today's news" in MyQuery:
            from getNews import todays_news
            todays_news()
        elif "today's latest news" in MyQuery:
            from getNews import todays_news
            todays_news()
        elif "latest news" in MyQuery:
            from getNews import todays_news
            todays_news()

        #open any installed app 
        elif "launch" in MyQuery:
            try:
                MyQuery = MyQuery.replace('open' , '')
                MyQuery = MyQuery.replace('sage' , '')
                MyQuery = MyQuery.replace('launch' , '')
                pyautogui.press('super')
                pyautogui.typewrite(MyQuery)
                pyautogui.press("enter")
            except:
                speak("sorry, i can't open this application right now.")

        #  browsing 
        elif "google" in MyQuery:
            from searchNow import searchGoogle
            searchGoogle(MyQuery)

        elif "youtube" in MyQuery:
            from searchNow import searchYoutube
            searchYoutube(MyQuery)

        elif "wikipedia" in MyQuery:
            from searchNow import searchWikipedia
            searchWikipedia(MyQuery)
        
        #  for media controls 
        elif "pause video" in MyQuery:
            pyautogui.press("k")
            speak("video is now paused")
        elif "play video" in MyQuery:
            pyautogui.press("k")
            speak("video played")
        elif "mute video" in MyQuery:
            pyautogui.press("m")
            speak("video is now  muted")

        elif "volume up" in MyQuery:
            from keyboard import volumeup
            volumeup()
        elif "full volume" in MyQuery:
            from keyboard import fullvolume
            fullvolume()
        elif "volume down" in MyQuery:
            from keyboard import volumedown
            volumedown()
                
        elif "forward video" in MyQuery:
            from keyboard import forward
            forward()
        elif "backward video" in MyQuery:
            from keyboard import backward
            backward()

        #camera and screenshots   
        elif "take screenshot" in MyQuery:
            image = pyautogui.screenshot()
            image.save("Screenshot.png")
            print("Screenshot is captured and saved.")
            speak("screenshot is captured and saved")

        elif "click my photo" in MyQuery:
            pyautogui.press("super") #windows key
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(3)
            speak("smile")
            pyautogui.press("enter")
            print("photo captured")
            speak("Photo captured.")
              
        # temperature & weather inforamtion
        elif "temperature" in MyQuery:
                    search = "temperature in nagpur"
                    url = f"https://www.google.com/search?q={search}"
                    req = requests.get(url)
                    data = BeautifulSoup(req.text , "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"Current {search} is {temp}")
                    speak(f"Current {search} is {temp}")
                
        elif "weather" in MyQuery:
                    search = "weather in nagpur"
                    url = f"https://www.google.com/search?q={search}"
                    req = requests.get(url)
                    data = BeautifulSoup(req.text , "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"Current {search} is {temp}")
                    speak(f"Current {search} is {temp}")

        #joke
        elif "tell me a joke" in MyQuery:
            joke=pyjokes.get_joke(language="en", category="all")
            print("Joke: ",joke)
            speak(joke)


        #time and date info
        elif "the time" in MyQuery:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Current time is",time)
            speak(f"Current time is {time}")

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

        # shutdown & restart
        elif "shut down my system" in MyQuery or "shutdown my system" in MyQuery:
            speak("Are you sure you want to shutdown your system")
            print("Say YES or NO")
            shutdown=command_me().lower()
            if "yes" in shutdown:
                speak("Now, shutting down the system, have a nice day")
                os.system("shutdown /s /t 1") #/s= seconds /t= time interval 1 is duration
            elif "no" in shutdown:
                break

        elif "restart my system" in MyQuery:
            speak("Are you sure you want to restart your system")
            print("Say YES or NO")
            restart=command_me().lower()
            if "yes" in restart:
                speak("Now, restarting the system, have a nice day")
                os.system("shutdown /r /t 1") #y=yes f=force
            elif "no" in restart:
                break

