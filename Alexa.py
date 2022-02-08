import speech_recognition as sr  # pip install SpeechRecognition ..
import pyttsx3  # pip install pyttsx3 ..
import pywhatkit  # pip install pywhatkit ..
import pyautogui  # pip install pyautogui
import wikipedia  # pip install wikipedia
import pyjokes  # pip install pyjokes
import requests  # pip install requests
import cv2  # pip install opencv-python
import PyPDF2  # pip install PyPDF2
import psutil  # pip install psutil
import speedtest  # pip install speedtest-cli
import wolframalpha  # pip install wolframalpha
import mysql.connector  # pip install mysql-connector
import webbrowser
import datetime
import os
import smtplib
from hurry.filesize import size  # pip install hurry.filesize
from googletrans import Translator  # pip install googletrans
from time import sleep
from email.message import EmailMessage
#  for people with python 3.9 and problem install pyaudio!!! you can install audio by:pip install pipwin then wait till its done. then: pipwin install pyaudio
#  pip install pynput
# signed up in wolframalpha, openweathermap

listener = sr.Recognizer()  # to listen the audio
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="alexa")
mycursor = mydb.cursor()

def wishMe():
    global mydb, mycursor
    mycursor.execute("select name from name")
    myresult = mycursor.fetchone()
    for myname in myresult:
        pass
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning" + myname)
    elif hour >= 12 and hour < 16:
        talk("Good Afternoon" + myname)
    else:
        talk("Good Evening!" + myname)
    talk("Iam Alexa. Please tell me how may I help you")

def take_command():
    try:
        with sr.Microphone() as source:  # source for audio
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def send_email(receiver, subject, message):  # import smtplib  # import speech_recognition as sr  # import pyttsx3  # from email.message import EmailMessage
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    a = pyautogui.prompt(text='Enter your MailID', title='Login Page', default='mukeshshankar2001@gmail.com')  # import pyautogui
    b = pyautogui.password(text='Enter your password', title='Login Page', default='', mask='*')  # import pyautogui
    server.login(a, b)
    email = EmailMessage()
    email['From'] = a
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def mail_id():
    global mydb, mycursor
    print('Enter name of the person you wanted to add : ')
    talk('Enter name of the person you wanted to add')
    name = take_command()
    talk('Enter mail address of ' + name)
    mail_add = input('Enter mail address of ' + name + ' : ')
    mycursor.execute("insert into mail_id values ('" + name + "','" + mail_add + "')")
    mydb.commit()
    print(name + ' Mail address added to database')
    talk(name + ' Mail address added to database')

def birthday():
    global mydb, mycursor
    print('Enter name of the person you wanted to add : ')
    talk('Enter name of the person you wanted to add')
    name = take_command()
    print('Enter the birthday date of ' + name + ' : ')
    talk('Enter the birthday date of ' + name)
    date = take_command()
    mycursor.execute("insert into birthday values ('" + name + "','" + date + "')")
    mydb.commit()
    print(name + ' birthday date added to database')
    talk(name + ' birthday date added to database')

def language():
    global mydb, mycursor
    print('Enter name of the language : ')
    talk('Enter name of the language')
    lang = take_command()
    print('Enter the birthday date of ' + lang + ' : ')
    talk('Enter the birthday date of ' + lang)
    lang_code = take_command()
    mycursor.execute("insert into language values ('" + lang + "','" + lang_code + "')")
    mydb.commit()
    print(lang + ' Language added to database')
    talk(lang + ' Language added to database')

if __name__ == "__main__":
    clear = lambda: os.system('cls')  # import os

    clear()
    wishMe()


def run_alexa():  # import speech recognition and pyaudio
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="alexa")
    mycursor = mydb.cursor()
    command = take_command()
    print(command)
    if 'play' in command:  # import pywhatkit
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        song = command.replace('play', '')
        print('playing ' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'search' in command:  # import pywhatkit
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        sear = command.replace('search ', '')
        print('searching ' + sear)
        talk('searching ' + sear)
        pywhatkit.search(sear)

    elif 'wikipedia' in command:  # import wikipedia
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        command = command.replace('wikipedia ', '')
        results = wikipedia.summary(command, sentence=2)
        talk('According to Wikipedia')
        print(results)
        talk(results)

    elif 'time' in command:  # import datetime
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)

    elif 'change my name' in command:
        print('Please tell me the name you wanted to change')
        talk('Please tell me the name you wanted to change')
        alt_name = take_command()
        mycursor.execute("update name set name = '" + alt_name + "'")
        mydb.commit()
        talk('Your name changed as ' + alt_name)

    elif 'date' in command:  # import datetime
        date = datetime.datetime.now().strftime('%d:%M %Y')
        print("Today's date is " + date)
        talk("Today's date is " + date)

    elif 'joke' in command:  # import pyjokes
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'are you single' in command:  # talk func is  called
        print('I am in a relationship with wifi')
        talk('I am in a relationship with wifi')

    elif 'how are you' in command:  # talk func is called
        mycursor.execute("select name from name")
        myresult = mycursor.fetchone()
        for myname in myresult:
            talk('I am fine ' + myname)
            talk('How are you')

    elif 'fine' in command or 'good' in command:  # talk func is called
        mycursor.execute("select name from name")
        myresult = mycursor.fetchone()
        for myname in myresult:
            talk("It's good to know that your fine " + myname)

    elif 'who created you' in command or 'who made you' in command:  # talk func is called
        mycursor.execute("select name from name")
        myresult = mycursor.fetchone()
        for myname in myresult:
            talk('God')
            talk('And his name is ' + myname)

    elif 'what is my name' in command or 'tell my name' in command:
        mycursor.execute("select name from name")
        myresult = mycursor.fetchone()
        for myname in myresult:
            print('We call you as ' + myname)
            talk('We call you as ' + myname)

    elif 'is love' in command:  # talk func is called
        talk('It is 7th sense that destroy all other sense and makes you non sense')

    elif 'where is' in command:  # import webbrowser
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        command = command.replace('where is', '')
        location = command
        talk('User asked to locate')
        talk(location)
        webbrowser.open('https://www.google.com/maps/place/' + location + '')

    elif 'open' in command:  # import webbrowser
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        opening = command.replace('open ', '')
        print('opening ' + opening)
        talk('opening ' + opening)
        if 'whatsapp' in opening:  # import webbrowser
            webbrowser.open('https://web.whatsapp.com/')
        elif 'google images' in opening:  # import webbrowser
            webbrowser.open('https://images.google.com/')
        elif 'brave' in opening:  # import os
            try:
                br = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
                os.startfile(br)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        elif 'telegram' in opening:  # import os
            try:
                tel = 'D:\\Telegram Desktop\\Telegram.exe'
                os.startfile(tel)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        elif 'vsdc' in opening:  # import os
            try:
                vsdc = 'D:\\FlashIntegro\\VideoEditor\\VideoEditor.exe'
                os.startfile(vsdc)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        elif 'vlc' in opening:  # import os
            try:
                vlc = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
                os.startfile(vlc)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        elif 'team viewer' in opening:  # import os
            try:
                team = "C:\\Program Files\\TeamViewer\\TeamViewer.exe"
                os.startfile(team)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        elif 'teamviewer' in opening:  # import os
            try:
                team = "C:\\Program Files\\TeamViewer\\TeamViewer.exe"
                os.startfile(team)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        elif 'snipping tool' in opening:  # import os
            try:
                sni_tool = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Snipping Tool"
                os.startfile(sni_tool)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        elif 'pycharm' in opening:  # import os
            try:
                pyc = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2021.1.2"
                os.startfile(pyc)
            except:
                webbrowser.open('https://www.' + opening + '.com')
        else:  # import webbrowser
            webbrowser.open('https://www.'+opening+'.com')

    elif 'add' in command:
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        command.replace('add ', '')
        if 'mail id' in command or 'mail address' in command or 'gmail address' in command or 'gmail id' in command:
            mail_id()
        elif 'birthday' in command:
            birthday()
        elif 'language' in command:
            language()
        else:
            pass

    elif 'youtuber' in command:  # import webbrowser
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        you = command.replace('youtuber ', '')
        print('opening youtuber ' + you)
        talk('opening youtuber ' + you)
        webbrowser.open('https://www.youtube.com/results?search_query=' + you)

    elif 'birthday of' in command:
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        you = command.replace('birthday of ', '')
        try:
            mycursor.execute("select date from birthday where name = '" + you + "'")
            bday = mycursor.fetchone()
            for x in bday:
                print("Birthday of " + you + " is " + x)
                talk("Birthday of " + you + " is " + x)
        except:
            print("There is no name you're searched for")
            talk("There is no name you're searched for")
            talk("Would you like add your friend's birthday date?")
            brth = take_command()
            if 'yes' in brth or 's' in brth:
                birthday()

    elif 'translate' in command:  # from googletrans import Translator
        trans = {
            'tamil': 'ta',
            'english': 'en',
            'hindi': 'hi',
            'french': 'fr',
            'swedish': 'sv',
            'telugu': 'te',
            'kannada': 'kn',
            'korean': 'ko',
            'malayalam': 'ml',
            'marathi': 'mr',
            'italian': 'it',
            'arabic': 'ar',
            'dutch': 'nl',
            'gujarati': 'gu'
        }
        translater = Translator()
        talk('Enter the word to translate')
        a = input('Enter the word to translate : ')
        talk('Enter the language')
        b = input('Enter the language : ')
        c = trans[b]
        out = translater.translate(a, dest=c)
        talk(out.text)
        print(out.text)

    elif 'weather in' in command:  # import request
        api_add = "https://api.openweathermap.org/data/2.5/weather?appid=ad93f8131735149776455326a67cc17b&q="
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        you = command.replace('weather in', '')
        url = api_add + you
        response = requests.get(url).json()
        if response["cod"] != "404":
            y = response["main"]
            current_temperature = y["temp"]
            current_temp = y["temp"] - 273.15
            fl = current_temp
            format_float = "{:.2f}".format(fl)
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = response["weather"]
            weather_description = z[0]["description"]
            print('Temperature (in kelvin unit) = ' + str(current_temperature))
            print('Temperature (in celcius unit) = ' + str(format_float))
            print('Atmospheric pressure (in hPa unit) = ' + str(current_pressure))
            print('Humidity (in percentage) = ' + str(current_humidiy))
            print('Description = ' + str(weather_description))
            talk('Temperature (in kelvin unit) = ' + str(current_temperature))
            talk('Temperature (in celcius unit) = ' + str(format_float))
            talk('Atmospheric pressure (in hPa unit) = ' + str(current_pressure))
            talk('Humidity (in percentage) = ' + str(current_humidiy))
            talk('Description = ' + str(weather_description))
        else:
            talk(" City Not Found ")

    elif 'climate in' in command:
        api_add = "https://api.openweathermap.org/data/2.5/weather?appid=ad93f8131735149776455326a67cc17b&q="
        command.replace(' ', '')  # to reduce unnecessary white space
        command = ' '.join(command.split())  # to give only one white space
        you = command.replace('climate in', '')
        url = api_add + you
        response = requests.get(url).json()
        if response["cod"] != "404":
            y = response["main"]
            current_temperature = y["temp"]
            current_temp = y["temp"] - 273.15
            fl = current_temp
            format_float = "{:.2f}".format(fl)
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = response["weather"]
            weather_description = z[0]["description"]
            print('Temperature (in kelvin unit) = ' + str(current_temperature))
            print('Temperature (in celcius unit) = ' + str(format_float))
            print('Atmospheric pressure (in hPa unit) = ' + str(current_pressure))
            print('Humidity (in percentage) = ' + str(current_humidiy))
            print('Description = ' + str(weather_description))
            talk('Temperature (in kelvin unit) = ' + str(current_temperature))
            talk('Temperature (in celcius unit) = ' + str(format_float))
            talk('Atmospheric pressure (in hPa unit) = ' + str(current_pressure))
            talk('Humidity (in percentage) = ' + str(current_humidiy))
            talk('Description = ' + str(weather_description))
        else:
            talk(" City Not Found ")

    elif 'turn on webcam' in command:  # import cv2
        talk('Turning on webcam')
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, frame = cam.read()
            if cv2.waitKey(10) == ord('q'):
                break
            cv2.imshow('Mukesh Cam', frame)

    elif 'pdf file' in command or 'audiobook' in command:  # import PyPDF2 # import pyttsx3
        talk('Enter your file name with the path and .pdf extension here')
        pdf = input('Enter your file name with the path and .pdf extension here : ')
        book = open(pdf, 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(pages)
        speaker = pyttsx3.init()
        for num in range(0, pages):
            page = pdfReader.getPage(0)
            text = page.extractText()
            print(text)
            speaker.say(text)
            speaker.runAndWait()

    elif 'battery' in command or 'charger' in command:  # import psutil
        battery = psutil.sensors_battery()
        percent = battery.percent
        print("Battery Percentage " + str(percent) + "% Remaining")
        talk("Battery Percentage " + str(percent) + "% Remaining")

    elif 'calculate' in command:  # import wolframalpha
        app_id = "6T8UL7-LYATRX7W7P"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate')
        query = command.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        talk("The answer is " + answer)

    elif 'speed test' in command or 'internet speed' in command or 'connection speed' in command or 'data speed' in command:  # import speedtest # from email.message import EmailMessage
        st = speedtest.Speedtest()
        talk('What do you want to test :\n1) Download Speed\n2) Upload Speed\n3) Both\nYour Choice :')
        print('What do you want to test :\n1) Download Speed\n2) Upload Speed\n3) Both\nYour Choice :')
        command = take_command()
        if 'Download Speed' in command:
            print("Connecting...")
            print("Downloading speed is : ", size(st.download()))
            talk("Downloading speed is : ", size(st.download()))
        elif 'Upload Speed' in command:
            print("Connecting...")
            print("Uploading speed is : ", size(st.upload()))
            talk("Uploading speed is : ", size(st.upload()))
        elif 'Both' in command:
            print("Connecting...")
            print("Downloading speed is : ", size(st.download()))
            talk("Downloading speed is : ", size(st.download()))
            print("Please Wait!!!")
            print("Uploading speed is : ", size(st.upload()))
            talk("Uploading speed is : ", size(st.upload()))
        else:
            print("Please choose an option!!")
            talk("Please choose an option!!")

    elif 'stop listening' in command:  # from time import sleep
        talk("for how much time you want me to stop listening")
        a = int(take_command())
        sleep(a)

    elif 'rest' in command or 'exit' in command or 'terminate' in command or 'end' in command or 'quit' in command or 'close' in command:  # exit() func is called
        talk('Ok, Iam going to take a nap...')
        exit()

    else:
        print('Please say the command again')
        talk('Please say the command again')

while True:
    run_alexa()
