import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!sir")

    else:
        speak("Good Evening!sir")

    speak(" Ï am Virtual Assistant,nice to see u... what are we doing today?")

def takecommand():
    # it takes microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("sir I'm ready to take commands")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        speak("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        speak(f"sir did you said: {query}\n")
        print(f"Command Taken: {query}\n")

    except Exception as e:
        #print(e)
        speak("Sorry sir I can't hear you...Please say that again ")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls('virtual-assistant email@gmail.com', 'virtual-assistant-password-here')
    server.sendmail('virtual-assistant email@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        
        # logic for executing tasks based on query
        if 'search' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stakeoverflow' in query:
            webbrowser.open("stakeoverflow.com")

        #COMMAND TO OPEN APPLICATIONS IN THE COMPUTER.
        elif "physics file" in query:
            physics = 'C:\\Users\\Srijan Samridh\\Desktop\\12th Boards prep\\Physics\\Alternating Current ch-7'
            lectures = os.listdir(physics)
            # print(lectures)
            os.startfile(os.path.join(physics, lectures[4])) #UPDATE WITH RANDOM MODULE--need to be updated

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "google chrome" in query:
            google = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
            os.startfile(google)

        elif "send email" in query:
            try:
                speak("what should I say?")
                content = takecommand()
                to = "yourIDemail@gmail.com"
                sendEmai(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir. I am unable to send this email.")
        elif "quit" in query:
            speak("okay sir, Have great day sir ")
            exit()
