import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
import pyautogui
import psutil
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  



    speak("I am Sittu Assistant. Please tell me how may I help you")       



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\aritra\\Desktop\\screenshot\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'what is' in query:
            person = query.replace('what is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        
        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
               
        elif 'how is the weather' and 'weather' in query:
            webbrowser.open("weather.com")

        
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        
        elif 'open document' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))


        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()
        elif 'do you know anything' in query:
            remember =open('data.txt', 'r')
            speak("you said me to remember that" +remember.read())
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ARITRA\\Desktop\\Assistant\\assistant.py"
            os.startfile(codePath)
        
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu'in query:
            cpu()


        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pabitrag858@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sittu. I am not able to send this email")    
