import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time

system = pyttsx3.init('sapi5')
voices = system.getProperty('voices')
system.setProperty('voice', voices[1].id)

def speak(audio):
    system.say(audio)
    system.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")   

    else:
        speak("Good Evening")  

    speak("I am Dora. what can i do for you dear")       

def myorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(2)
        clearscreen()
        print("Listening command...")
        speak("Listening command...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        clearscreen()
        print("Recognizing your command, dear...")  
        speak("Recognizing your command, dear...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        time.sleep(2)
        clearscreen()
        print(e)    
        print("Say that again please...")  
        speak("Say that again please...")
        return "None"
    return query

def clearscreen():
    os.system('cls')


if __name__ == "__main__":
    greetings()
    while True:
 
        query = myorder().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Wikipedia says")
            print(results)
            speak(results)

        elif 'exit' in query:
            speak("pleasure to serve you my friend")
            exit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")    

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Dear, the time is {strTime}")

        elif 'code studio' in query:
            try:
                path="C:\\Users\\my world\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(path)
            except Exception as e:
                speak('no such apps found, dear')    

        elif 'joke' in query or 'tell me a joke' in query:
            speak('Do u know types of java......') 
            time.sleep(2)
            speak('hahahahahahaha marjava,lootjava,hai may sadkay java hahahahahaha')  

        elif 'who are you' in query:
            speak('i am dora, your virtual best friend')

        elif 'how are you' in query:
            speak('I am fine, thank you and how are you, dear')

        elif 'am fine' in query or 'am okey' in query:
            speak('good to hear that, dear')          
    