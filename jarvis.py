# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:12:25 2020

@author: Pushkar
"""
import pyttsx3
import datetime
import speech_recognition as SR
import wikipedia 
import smtplib #for email
import webbrowser
import os
import pyautogui #for screenshot
import psutil #for system status
import pyjokes #for jokes
#import requests, json
from geopy.geocoders import Nominatim
#import gmaps
import re
import sys
import cv2
from chitchat import *
from horoscope_generator import HoroscopeGenerator
engine = pyttsx3.init()

with open('C:/Users/Pushkar/Documents/Jarvis/details.txt') as f:
    username = f.readline()
    password = f.readline()
f.close()

with open('C:/Users/Pushkar/Documents/Jarvis/APIkey.txt') as f:
        api_key = f.readline()
f.close()
with open('C:/Users/Pushkar/Documents/Jarvis/APIkeyWeather.txt') as f:
        api_key_weather = f.readline()
f.close()
with open('C:/Users/Pushkar/Documents/Jarvis/googleapi.txt') as f:
        api_key_google = f.readline()
f.close()
def speak(audio):
    engine.say(audio)
    engine.setProperty('rate', 150)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', voice_id)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak('Current time is')
    speak(time)
    
def date():
    date1 = datetime.datetime.now().strftime("%d-%B-%Y")
    speak('Current date is')
    speak(date1)

def greet():
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good Moring Pushkar')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    elif hour >= 18 and hour < 23.59:
        speak('Good Evening')
    else:
        speak('Good night')
    speak('Welcome back!!')
    speak('How may i help you?')

def acceptCommand():
    p = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening.....")
        p.pause_threshold = 1
        audio = p.listen(source)
    try:
        print("Recognizing....")
        query = p.recognize_google(audio,language = 'en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Cannot hear you")
        sys.exit(0)
        return None
    return query

def email(to, mail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(username, to, mail)
    server.close()

def remember():
    speak("what should I remember?")
    data = acceptCommand()
    speak("You asked me to remember" + data)
    remem = open('data.txt', 'w')
    remem.write(data)
    remem.close()

def remember1():
      f = open('data.txt', 'r')
      speak('you told me to remember'+f.read())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Pushkar/Pictures/Jarvis Screenshots/screenshot_by_Jarvis.png')

def systemStatus():
    ss = psutil.sensors_battery()
    speak("Battery percentage is ")
    speak(ss.percent)
    speak("percent")
    if ss.power_plugged == False:
        speak("Charger is not plugged")
        hours = ss.secsleft/3600
        speak("Time left is ")
        speak("%.2f"%hours)
        speak("hours")
    else:
        speak("Charger is plugged")
    CPU = str(psutil.cpu_percent())
    speak("CPU usage is + "+ CPU)

def jokes():
    speak(pyjokes.get_joke())
    speak('If you liked a joke laugh hahahahaha')
    speak('Much appreciated')

def weather():

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    speak("please give me name of your city")
    q = acceptCommand()
    CITY = q
    API_KEY = api_key_weather
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       temperature = main['temp']
       temperature = temperature - 273.15
       humidity = main['humidity']
       pressure = main['pressure']
       report = data['weather']
       speak("Your city :"+ CITY)
       speak("temperature is " + str("%.2f"%temperature)+"degree celcius")
       speak(f"Humidity is: {humidity}")
       speak(f"Pressure is : {pressure}")
       speak(f"Weather Report for pune: {report[0]['description']}")
    else:
       print("Error in the HTTP request")

def maps():
    geolocator = Nominatim(user_agent='Jarvis')
    base = 'https://api.tomtom.com/routing/1/calculateRoute/'
    base1 = 'https://www.google.com/maps/dir/'
    speak("Whats your location")
    origin = acceptCommand()
    origin = geolocator.geocode(origin)
    origin1 = str(origin)
    origin1 = re.sub(r'[^\w\s]','',origin1)
    origin1 = origin1.split()
    print(origin1[0])
    print(origin.latitude, origin.longitude)
    speak("Where do you want to go")
    destination = acceptCommand()
    destination = geolocator.geocode(destination)
    destination1 = str(destination)
    destination1= re.sub(r'[^\w\s]','',destination1)
    destination1 = destination1.split()
    print(destination1[0])
    print(destination.latitude, destination.longitude)
   # speak("Mode of transport")
   # mode1 = acceptCommand()
    URL = base + str(origin.latitude) + ',' + str(origin.longitude) + ':' + str(destination.latitude) + ',' + str(destination.longitude) + '/json?key='+api_key
    print(URL)
    URL2 = base1 + str(origin1[0]) + '/' + str(destination1[0])
   # print(URL2)
    responses = requests.get(URL)
    if responses.status_code == 200:
        data = responses.json()
        print(data)
    webbrowser.open(URL2)

def googlesearch():
    base = 'https://www.google.com/search?q='
    speak("What do you want to google?")
    q = acceptCommand()
    URL = base + q
    speak("here are your results!")
    webbrowser.open(URL)
       
def capture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0 

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        
        k = cv2.waitKey(1)
        q = acceptCommand().lower()
        
        if k%256 == 27 or q == 'close':
            print("Escape hit, closing...")
            speak("closing")
            break
        elif k%256 == 32 or q == 'capture':
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite('C:/Users/Pushkar/Pictures/Jarvis Cameraroll/{}'.format(img_name), frame)
            print("{} written!".format(img_name))
            img_counter += 1
            speak("Done")
    cam.release()
    cv2.destroyAllWindows()

def horoscope():
    speak(HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence()))
   
if __name__ == '__main__':
    greet()
    while True:
        query = acceptCommand().lower()
        if 'bye' in query:
            speak('Have a nice day')
            break
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching on Wikipedia..')
            query = query.replace('wikipedia', ' ')
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif 'mail' in query:
            try:
                speak('What should I send?')
                content = acceptCommand()
                speak(content)
                to = ''
                speak(to)
                email(to, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'amazon' in query:
            webbrowser.open('www.amazon.in')
        elif 'flipkart' in query:
            webbrowser.open('www.flipkart.com')
        elif 'facebook' in query:
            webbrowser.open('www.facebook.com')
        elif 'logout' in query:
            speak('are you sure you want to shutdown pc?')
            if 'yes' in query:
                os.system('shutdown -l')
            else:
                quit()
        elif 'shutdown' in query:
            speak('are you sure you want to shutdown pc?')
            if 'yes' in query:
                os.system('shutdown /s /t 1')
            else:
                quit()
        elif 'restart' in query:
            speak('are you sure you want to restart pc?')
            if 'yes' in query:
                os.system('shutdown /r /t 1')
            else:
                quit()
        elif 'music' in query:
            if 'on youtube' in query:
                speak('Opening Youtube')
                webbrowser.open('https://www.youtube.com/watch?v=bzW9fmwcmG4&list=RDbzW9fmwcmG4&start_radio=1&t=0')
            else:
                songs_dir = "C:/Users/Pushkar/Music"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'remember that' in query:
            remember()
        elif 'do you remember' in query:
            remember1()
        elif 'screenshot' in query:
            screenshot()
            speak('Done!!')
        elif 'system status' in query:
            systemStatus()
        elif 'joke' in query:
            jokes()
        elif 'weather' in query:
            weather()
        elif 'direction' in query:
            maps()
        elif 'maps' in query:
            webbrowser.open('maps.google.com')
        elif 'google' in query:
            googlesearch()
        elif 'click photo' in query:
            capture()
        elif 'horoscope' in query:
            horoscope()
        elif 'who are you' in query:
            who_are_you()
        elif 'how are you' in query: 
            how_are_you()
        elif 'who is pushkar' in query:    
            who_is_pushkar()
        elif 'toss a coin' in query:   
            toss_coin()
        elif 'when were you born' in query:   
            when_were_you_born()
        elif 'are you smart' in query:  
            are_you_smart()
        elif 'are you human' in query: 
            are_you_human()
        elif 'will you marry me' in query:  
            will_you_marry_me()
        elif 'i love you' in query: 
            i_love_you()
        elif 'how do i look' in query:
            How_do_i_look()
        elif ' ' in query:
            undefined()
            break