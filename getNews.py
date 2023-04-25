import pstats
import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 190)

def speak(audio):
    engine.say(audio)    
    engine.runAndWait()  

r= sr.Recognizer()

def command_me():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5) #to recognize threshold noise level--pehele 0.2 pr test kiya tha
        print("Listening...")
        audio1=r.listen(source) #get input from user

        MyQuery=r.recognize_google(audio1, language='en-in') #using google to recognize audio
        MyQuery=MyQuery.lower()
        #speak(MyQuery)
        return MyQuery
    

def todays_news():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e5eeda4cd17f4560823d150052daf4cb" , 
    "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e5eeda4cd17f4560823d150052daf4cb" , 
    "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e5eeda4cd17f4560823d150052daf4cb" ,
    "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e5eeda4cd17f4560823d150052daf4cb" , 
    "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e5eeda4cd17f4560823d150052daf4cb", 
    "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e5eeda4cd17f4560823d150052daf4cb"}

    content = None
    url = None

    
    print("Select the news field:-")
    print("1.Business\n2.Entertainment\n3.Sports\n4.Science\n5.Technology\n6.Health\n")
    speak("Which field news do you want, [business], [entertainment], [sports], [science], [technology], [health]")
    

    field=command_me().lower()
    print("You said- "+field)


    for key , value in apidict.items():
        if field in key: #if key.lower() in field.lower():
            url=value
            print(url)
            print("url was found\n")
            break
        else:
            url = True

    if url is True:
        print("url not found\n")

    news = requests.get( url).text
    news = json.loads(news)
    speak("Here is the first news:\n")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"\nfor more info visit:  {news_url}\n")

    

        speak("would you like to continue or stop")
        x=command_me().lower()
        if "continue" in x :
            pass
        elif "stop" in x :
            break

    speak("that's all, is there anything else i can help you with")
