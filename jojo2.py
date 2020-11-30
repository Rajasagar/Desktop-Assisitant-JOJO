import pyttsx3
import pygame
import webbrowser
import smtplib
#import config
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import requests
import urllib
from PyDictionary import PyDictionary
from nltk.corpus import wordnet
import ety
from googlesearch import search
import feedparser
#from win32com.client import Dispatch

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('JU5PGQ-YGLTHR8VXV')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


def speak(audio):
    print('jojo: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your desktop assistant, jojo  ')
speak('How may I help you sir ?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
         r = sr.Recognizer()                                                                                   
         with sr.Microphone() as source: 
            
             speak('Sorry sir! I didn\'t get that! Try again !')                                                                      
             print("Listening...")
             r.pause_threshold =  1
             audio = r.listen(source)
             
         try:
             query = r.recognize_google(audio, language='en-in')
             print('User: ' + query + '\n')
             
         except sr.UnknownValueError:
             speak('Sorry sir! I didn\'t get that! Try typing the command!')
             query = str(input('Command: '))

    return query

def myCommand1():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
def playOnYoutube(query_string):
    query_string = urllib.parse.urlencode({"search_query" : query})
    search_string = str("http://www.youtube.com/results?" + query_string)
    speak("Here's what you asked for. Enjoy!")
    webbrowser.open_new_tab(search_string)
    

def searchOnGoogle(query, outputList):
    speak('The top five search results from Google  are listed below.')
    for output in search(query, tld="co.in", num=10, stop=5, pause=2):
        print(output)
        outputList.append(output)
    return outputList


def openLink(outputList):
    speak("Here's the first link for you.")
    webbrowser.open(outputList[0])    
    

def getNews(url):
    for entry in getFeeds(url):
        article_title = entry.title
        #article_description = entry.description
        speak("Heading: {}".format(article_title))
      #  print("Description: {}\n".format(article_description)) 
      

def getFeeds(url):
    feed = feedparser.parse(url)
    feed_entries = feed.entries
    return feed_entries

def newsFeeds(news_type):
    speak('Searching news for you from NDTV India')
    if (news_type in latestnews_url):
        speak(getNews(latestnews_url))
    if (news_type in topnews_url):
        speak(getNews(topnews_url))
    if (news_type in worldnews_url):
        speak(getNews(worldnews_url))
    if (news_type in sport_url):
        speak(getNews(sport_url))
    if (news_type in gadgetsnews_url):
        speak(getNews(gadgetsnews_url))
        
sport_url = "http://feeds.feedburner.com/ndtvsports-latest"
topnews_url = "http://feeds.feedburner.com/ndtvnews-top-stories"
worldnews_url = "http://feeds.feedburner.com/ndtvnews-world-news"
latestnews_url = "http://feeds.feedburner.com/ndtvnews-latest"
gadgetsnews_url = "http://feeds.feedburner.com/gadgets360-latest"
        
    
    
def getCompleteInfo(word):
    dictionary = PyDictionary()
    mean = {}
    mean = dictionary.meaning(word)
    synonyms = []
    antonyms = []

    speak("Alright. Here is the information you asked for.")

    for key in mean.keys():
        speak("When "+str(word)+" is used as a "+str(key)+" then it has the following meanings")
        for val in mean[key]:
            print(val)
        print()


    speak("The possible synonyms and antonyms of "+str(word)+" are given below.")
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas():
            if l.name() not in synonyms:
                synonyms.append(l.name())
            if l.antonyms() and l.antonyms()[0].name() not in antonyms:
                antonyms.append(l.antonyms()[0].name())
    
    print("Synonyms: ", end = " ")
    print(' '.join(synonyms), end = " ")
    print("\n")
    print("Antonyms: ", end = " ")
    print(' '.join(antonyms), end = " ") 
    print("\n")

    ori = ety.origins(word)
    if len(ori) > 0:
        speak("There are "+str(len(ori))+" possible origins found.")
        for origin in ori:
            print(origin)
    else:
        speak("I'm sorry. No data regarding the origin of "+str(word)+" was found.")

    


    
if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        
        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            
            speak('okay')
        elif 'play on youtube' in query:    
            speak('What should I look up for ?')
            query = myCommand()
            playOnYoutube(query)
        
        elif 'open dictionary' in query or 'dictionary' in query:
            speak('What word should I look up for ?')
            word = myCommand()
            getCompleteInfo(word)
        
        elif 'news' in query:
            news_type = ['sport', 'top', 'latest', 'world', 'gadget']
            speak("Which type of news you  want know ")
            news=myCommand()

            if (news in news_type):
            # search query for news
                try:
                    [newsFeeds(q_str) for q_str in news_type if news in q_str]
                    
                except:
                   # speak('Next command!  sir!')
                    #myCommand()
                    pass


            
            
        elif 'search' in query or 'search something for me' in query or 'search something ' in query  :
            outputList = []
            speak('What should I search for ?')
            query = myCommand()
            searchOnGoogle(query, outputList)
            speak('Should I open up the first link for you ?')
            query = myCommand()
            if 'yes' in query or 'sure' in query:
                openLink(outputList)
            if 'no' in query:
                speak('Alright.')

     
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
            
        elif 'open instagram' in query:
            speak('okay')
            webbrowser.open('www.instagram.com')

        elif 'open website' in query:
            speak('which website')
            website = myCommand()
            webbrowser.open('www.'+website+'.com')
        
        elif 'download song' in query:
            speak('which song')
            song = myCommand()
            webbrowser.open('download '+song+' song')
                    
        elif 'show image' in query or 'open image' in query or 'view image' in query:
            speak('whose image')
            image = myCommand()
            webbrowser.open('image of '+image)
                
        elif 'shutdown' in query:
            speak('system is going to shutdown')
            os.system("shutdown /s")
        
        elif 'restart' in query:
            speak('system is going to shutdown')
            os.system("shutdown /r")
            

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'send mail' in query or 'send email' in query:
            
                try:
                    speak('username of the reciever ')
                    reciever = myCommand()
                    reciever = reciever.lower()
                    reciever = reciever.replace(' dot','.')
                    
                    reciever1=''
                    for ch in reciever:
                        if ch==' ':
                            pass
                        else:
                            reciever1 = reciever1 + ch
                            
                    speak('check the username is correct or not......say YES or NO')
                    
                    print('username - ',reciever1)
                    check = myCommand1()
                    check = check.lower()
                    
                    if(check=='yes'):
                    
                        speak('What should I say? ')
                        content = myCommand()
                    
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login("jojojameela69@gmail.com", 'JoJoJameela69')
                        server.sendmail('jojojameela69@gmail.com', reciever1+"@gmail.com", content)
                        server.close()
                        speak('Email sent!')
                    
                    else:
                        speak('type the user name ')
                        reciever1 = str(input('Command: ')) 
                       
                        speak('What should I say? ')
                        content = myCommand()
                    
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login("jojojameela69@gmail.com", 'JoJoJameela69')
                        server.sendmail('jojojameela69@gmail.com', reciever1+"@gmail.com", content)
                        server.close()
                        speak('Email sent!')
                       
                    
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or ' so stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
            
        if ('sleep mode') in query:
            
            speak('ok sir, i am on sleeping mode')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')     
            
        elif 'jojo tell me a joke' in query or 'jojo tell me jokes' in query or 'tell me a joke jojo' in query or 'joke' in query:
             res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
             if res.status_code == requests.codes.ok:
                  speak('here is a joke for you sir !') 
                  speak(str(res.json()['joke']))
                  
             else:
                  speak('oops!I ran out of jokes')
                  
             speak(' would you like more jokes sir...YES or NO') 
             check = myCommand1()
             check = check.lower()
             if(check=='yes'):
                 res = requests.get(
                'https://icanhazdadjoke.com/',
                 headers={"Accept":"application/json"}
                        )
                 if res.status_code == requests.codes.ok:
                     
                    speak('here is a joke for you sir !') 
                    speak(str(res.json()['joke']))
             
   
        elif 'play music' in query :
            
            folder = 'C:\\Users\\Raja Sagar\\OneDrive\\Documents\\music\\'            
            b_music = ['Muchh (1)','Muchh (2)','Muchh (3)']
            pygame.mixer.init()
            pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(-1)
            
                  
            speak('Okay, here is your music! Enjoy!')
            
        elif 'stop music' in query or 'stop the music' in query or 'stop the song' in query:
            
            pygame.mixer.music.stop()

        else:
            query = query
            speak('Wait, i am Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('i got it...sir')
                    speak('WOLFRAM-ALPHA says - ')
                    
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('i got it... sir')
                    speak('WIKIPEDIA says - ')
                    speak(results)
                    
                    
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        
