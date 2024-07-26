#for communicating with python
import pyttsx3
#for speech to text
import speech_recognition as sr
#for searching on platforms
import pywhatkit
#for stock market
import yfinance as yf
#for jokes and humor
import pyjokes
#opening web browser from code
import webbrowser
import datetime
import wikipedia

#voice to text
def transform_audio_into_text():

    #store recognizer in var
    r=sr.Recognizer()

    #set microphone
    with sr.Microphone() as source:

        #waiting time for initializing microphone
        r.pause_threshold=0.8

        #report for recording has begun
        print("Sqeak now!!!")

        #save the recording as audio
        audio=r.listen(source)

        try:
            #search on Google params as source,language
            request=r.recognize_google(audio,language="en-gb")

            #text to be tested
            print("you said "+request)

            #returning request
            return request

        #In case of error in understanding
        except sr.UnknownValueError:
            #Error proof
            print("oopsie!!! INVALID")
            #return error
            return ("Still waiting")

        #Incase can't be resolved
        except sr.RequestError:
            # Error proof
            print("oopsie!!! INVALID REQ")
            # return error
            return ("Still waiting")
        #unexpected error
        except:
            # Error proof
            print("oopsie!!! Something went wrong")
            # return error
            return ("Still waiting")

#speaking assistant
id1='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

def speak(message):
    #start engine with pyttsx3
    engine=pyttsx3.init()
    engine.setProperty('voice',id1)
    #delivering the message
    engine.say(message)
    engine.runAndWait()


#engine=pyttsx3.init()
#for checking installed voices
#for voice in engine.getProperty('voices'):
#    print(voice)


#day of week
def ask_day():
    #var with today's info
    day=datetime.datetime.today()
    #day of week
    week_day=day.weekday()
    #Names of days dictionary
    calendar={0:'Monday',
              1:'Tuesday',
              2:'Wednesday',
              3:'Thursday',
              4:'Friday',
              5:'Saturday',
              6:'Sunday'}

    day_today=f'Today its {calendar[week_day]}'
    speak(day_today)
#ask_day()
def ask_time():
    time=datetime.datetime.now()
    time=f"Now it is {time.hour} hours and {time.minute} minutes"
    speak(time)

#ask_time()


#initial greeting
def initial_greeting():
    speak("Hello, I am Wallah. How can I help you? say goodbye to close me down")

#main func of assistant
def my_assistant():
    initial_greeting()
    #cut off var for while loop
    go_on=True
    while go_on:
        #activate mic and save request
        my_request=transform_audio_into_text().lower()
        if 'open youtube' in my_request:
            speak('Sure, opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            webbrowser.open('https://www.google.com')
            continue
        elif 'today' in my_request:
            ask_day()
            continue
        elif 'what time it is' in my_request:
            ask_time()
            continue
        #elif 'do a wikipedia search for' or 'do a wikipedia search on' in my_request:
        #    speak('I am on it')
         #   my_request=my_request.replace('do a wikipedia search for','')
        #    answer=wikipedia.summary(my_request,sentences=1)
        #    speak('according to wikipedia:')
        #    speak(answer)
        #    continue

        elif 'google' in my_request:
            speak('searching')
            my_request=my_request.replace('google','')
            pywhatkit.search(my_request)
            speak('this is what i found from sources')
            continue
        elif 'play' in my_request:
            speak('playing it shortly')
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in my_request:
            share=my_request.split()[-2].strip()
            #matching with tikr
            portfolio={'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                searched_stock=portfolio[share]
                searched_stock=yf.Ticker(searched_stock)
                #key input on ticker
                price=searched_stock.info['regularMarketPrice']
                speak(f'The price of {share} is {price}')
                continue
            except:
                speak('I am sorry')
        elif 'goodbye' in my_request:
            speak('I am closing down. Wake me up if you need anything')
            break
my_assistant()

#voice option


#speak("Hope you're well. Have a nice day ahead")





