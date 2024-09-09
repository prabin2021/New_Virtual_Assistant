from basic_functions.basic_functionalities import *
from battery_status.battery_check import *
from camera_automation.open_camera import *
from email_automation.send_email import *
from google_automation.google_search import *
from greetings.greeting import *
from jarvis_status.jarvis_mode import *
from joke.jokes_teller import *
from queries_handling_functions.query_handle import *
from routine_handling.routine_sayer import *
from sentiment_analyzer.sentiment_analyze import *
from youtube_automation.search_on_youtube import *
from data_required.dialogues import *
from wikipedia_search_automation.wiki_search import *
from whatsapp_automation.whatsapp_automate import *
from translate_automation.translate import *
from last_activity_automation.last_actitivty_track import *
import pyttsx3
import speech_recognition as sr
import pyautogui
import urllib.parse
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess as sp
import cv2
import smtplib
import tkinter as tk
import pywhatkit as kit
import webbrowser
from datetime import datetime
from sketchpy import library as lib
from random import choice
from PIL import Image, ImageTk
import requests
import wikipedia
import sys
import subprocess
from mtranslate import translate
from colorama import Fore,Style,init
import threading
import psutil
import re
from transformers import pipeline
import logging
import time
import numpy as np

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 140)

engine.setProperty('voice', voices[2].id)

  # Set voice to female voice
logging.basicConfig(level=logging.INFO)
listening = True
recognizer = sr.Recognizer()
microphone = sr.Microphone()
sentiment_checked = False

def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_user_input():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        recognizer.pause_threshold = 2
        recognizer.energy_threshold = 250
        audio = recognizer.listen(source,5,10)

        # audio_data = audio.get_raw_data(convert_rate=44100, convert_width=2)
        # reduced_noise = nr.reduce_noise(audio_data)
    query = None
    try:
        print("Trying to recognize as Nepali language...")
        query1 = recognizer.recognize_google(audio, language="ne")
        query_translated = translate(query1,to_language="en")
        print("You said:", query_translated)
        query = query_translated.lower()
    except sr.UnknownValueError:
        try:
            print("Trying to recognize as English language...")
            query1 = recognizer.recognize_google(audio, language="en")
            query= query1.lower()
            print("You said:", query)
        except sr.UnknownValueError:
            print("Unable to recognize...")
            return None
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service. Please try again.")
            return None
    if not query:
        return None
    
    return query

    
def activate_assistant():
    speak("Sir, I am your virtual assistant Jarvis. Can I activate, sir?")
    activate_command = take_user_input()
    activation_phrases = [
        "yes bro you can activate",
        "okay sure",
        "i need you",
        "let's work together",
        "yes",
        "sure",
        "off course",
        "of course",
        "ofcourse",
        "go ahead",
        "activate now",
        "ok you can",
        "yes you can",
        "switch on",
        "activate and work",
        "you can start",
        "let's start",
        "you can activate",
    ]

    if activate_command is None:
        speak("Assistant not activated. Let me know when you need me, sir.")
    else:
        if any(phrase in activate_command for phrase in activation_phrases):
            speak("Activating now,sir!")
            main()
def process_command(query):   
    global sentiment_checked 
    global listening
    if listening:
        if not sentiment_checked:
            sentiment, confidence = analyze_sentiment(query)
            print(f"Your Sentiment: {sentiment}, Your Confidence: {confidence:.2f}")
            if sentiment == 'NEGATIVE' and confidence > 0.7:
                speak("I sense some negativity in your voice. Is everything alright sir?")
            sentiment_checked = True

        if "open camera" in query or "camera" in query or "open the camera" in query:
            open_camera()
            return "Camera opened sir"
        if "capture my photo" in query or "click my photo" in query or "picture " in query:
            capture_photo()
            return "Photo captured sucessfully sir"
        if  "open youtube" in query or "youtube" in query:
            speak("Sure sir, what would you like to watch on YouTube?")
            query = take_user_input()
            if query == "exit":
                return 
            search_query = extract_search_query(query)
            print("Search query:",search_query)
            search_youtube(search_query)
            return search_query
        if "open command prompt" in query or "command prompt" in query or "command line interface" in query:
            open_cmd()
            return "Command Prompt opened sir"
        if 'open notepad' in query:
            open_notepad()
            return "Notepad opened sir"
        if "time" in query:
            # current_hour = datetime.now().hour
            strTime = datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is " + strTime)
            return strTime
        if "cursor" in query or "eye" in query or "eyes" in query:
            speak("Ok, sure sir, I am working on it and please keep your eyes in front of the camera.")
            try:
                sp.run(['python','D:\\Environments\\eyecursor.py'])
            except FileNotFoundError:
                print("Error: The eyecursor.py script was not found.")
            except sp.CalledProcessError as e:
                print("Error executing eyecursor.py:", e)
        if "minimize" in query or "minimise" in query:
            speak("Ok sir, I am minimizing it.")
            pyautogui.hotkey('win','down','down')
            return "Window minimized sir"
        if "maximize" in query or "maximise" in query:
            speak("Ok sir, I am maximizing it.")
            pyautogui.hotkey('win','up','up')
            return "Window maximized sir"
        if "cloze the window" in query or "close the window" in query or "close window" in query or "close this window" in query:
            speak("Ok sir, I am closing it.")
            pyautogui.hotkey('ctrl','w')
            return "Window closed sir"
        if "class routine" in query or "routine" in query:
            speak("Ok sir, getting your class routine ")
            routineresult = handle_routine(query)
            return routineresult
        if "draw" in query or "Tony Stark" in query or "sketch" in query:
            speak("Drawing sir")
            obj = lib.rdj()
            obj.draw()
            return None
        if  "greet me" in query or "greet" in query:
            greet_user()
            return None
        if  "send mail" in query or "send an email" in query or "send email" in query or "send e-mail" in query or "send the email" in query:
            result_email = send_email()
            return result_email
        if "translate the word" in query or "translate word" in query or "translate texts" in query or "translate text" in query or "translate the text" in query:
            speak("Ok sure sir, please specify what do you want to translate")
            query1 = take_user_input()
            translate_text(query1)
            return None
        if "check battery percentage" in query or "battery percentage" in query or "battery status" in query or "check the battery percentage" in query:
            battey_persentage()

        if "tell me a joke" in query or "tell me the jokes" in query or "say me a joke" in query or "let's hear a joke" in query:
            joke = tell_random_joke()
            return joke
        if "search for" in query or "search in google" in query or "google" in query:
            search_google(query)
            return None
        if "open whatsapp" in query or "open the whatsapp" in query or "whatsapp" in query:
            speak("Sure sir.")
            open_whatsapp()
            return None
        if  "use wikipedia" in query or "wikipedia" in query:
            speak("Sure sir, what would you like to search for?")
            query = take_user_input()
            if query == "exit":
                return 
            extract_search_Query(query)
            return None
        if "jarvis sleep" in query or "sleep for a while" in query or "sleep" in query:
            toggle_jarwis_mode("sleep")
            listening = False
            return None
        if  "last activity" in query or "last activities" in query:
            remind_last_activity()
            return None
        if "class routine" in query or "routine" in query:
            handle_routine(query)
        
    if "jarvis wake up" in query or "wake up" in query or "wakeup" in query:
            print("Wake up command detected")
            toggle_jarwis_mode("wake up")
            listening = True
            return None
    if "exit" in query or "stop" in query or "quit" in query or "good night" in query:
            current_hour = datetime.now().hour
            if current_hour >= 21 or current_hour < 6:
                speak("Good night, sir. Take care!, and please wake me up when you feel bored or if any help needed.")
            else:
                speak("Have a good day, sir!, and please wake me up when you feel bored or if any help needed.")
            return "exit"
    if listening == False:
        print("Jarvis is sleeping. Discarding command.")
        return "sleeping"
    
def main():
    import threading
    from Face_Verification.Face_recognition import recognize_user
    speak("verifying your face.")
    verified = recognize_user()
    verifiednum = int(verified)
    if verifiednum > 40: 
        speak("Face verified sir")  
        # pyautogui.press('escape')
        cv2.destroyAllWindows()
        greet_user()
        # remind_last_activity()
        activity_thread = threading.Thread(target=monitor_activities)
        activity_thread.daemon = True
        activity_thread.start()
        while True:
            user_input = take_user_input()
            if user_input:
                result = process_command(user_input)
                if result == "exit":  
                    break
                if result != "sleeping":
                    result = handle_query(user_input)

            else: 
                continue
    else:
        speak("Face Not Verified. Please try again")
        pass

# if __name__ == "__main__":
#     activate_assistant()


from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

# Initialize GUI
from tkinter import Tk, Button, WORD, NORMAL, DISABLED, END, BOTH
from PIL import Image, ImageTk

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

def initialize_gui():
    global root, chat_box, microphone_button, clear_button

    speak("Hi sir, I am Jarvis your virtual assistant")
    def append_to_chat_box(text, is_user=False):
        chat_box.config(state=NORMAL)
        if is_user:
            chat_box.insert(END, f"User: {text}\n", 'user')
        else:
            chat_box.insert(END, f"Jarvis: {text}\n", 'jarvis')
        chat_box.config(state=DISABLED)
        chat_box.yview(END)
        root.update()

    def take_user_input_and_process():
        chat_box.config(state=NORMAL)
        chat_box.insert(END, "Jarvis: Listening...\n", 'jarvis')
        chat_box.config(state=DISABLED)
        chat_box.yview(END)
        root.update()
        query = take_user_input()
        if query:
            append_to_chat_box(query, is_user=True)

            response = process_command(query)
            response1 = handle_query(query)
            
            if response and isinstance(response, str):
                append_to_chat_box(response)
            elif callable(response):
                response_text = response()  # If it's a callable function, execute it and get the result
                append_to_chat_box(response_text)
            
            if response1 and isinstance(response1, str):
                append_to_chat_box(response1)
            elif callable(response1):
                response1_text = response1()  # If it's a callable function, execute it and get the result
                append_to_chat_box(response1_text)
    root = Tk()
    root.title("Jarvis Virtual Assistant")
    root.geometry("600x500")
    icon_image = Image.open("D:/Jarwis_Pro/jarwis2/logo.png")  # Ensure the icon file is in the specified path
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)

    # Set background color
    root.configure(bg="skyblue")

    # Create a frame for the chat box and buttons
    frame = Frame(root, bg="skyblue")
    frame.pack(expand=TRUE, fill=BOTH)

    # Add chat box
    chat_box = ScrolledText(frame, wrap=WORD, state=DISABLED, bg="lightyellow", fg="black", font=("Arial", 12))
    chat_box.tag_configure('user', foreground='red')
    chat_box.tag_configure('jarvis', foreground='blue')
    chat_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Load and add microphone button with custom image
    mic_image = Image.open("D:/Jarwis_Pro/jarwis2/micimg.jpg")  # Ensure this image is in your project folder
    mic_image = mic_image.resize((60, 60), Image.LANCZOS)  # Resize to fit your needs
    mic_image = ImageTk.PhotoImage(mic_image)
    microphone_button = Button(frame, image=mic_image, command=take_user_input_and_process, bd=0, bg="skyblue", relief=RAISED, activebackground="lightblue")
    microphone_button.grid(row=1, column=0, pady=10)

    # Load and add clear button with custom image
    clear_image = Image.open("D:/Jarwis_Pro/jarwis2/clrimg.jpeg")  # Ensure this image is in your project folder
    clear_image = clear_image.resize((60, 60), Image.LANCZOS)  # Resize to fit your needs
    clear_image = ImageTk.PhotoImage(clear_image)
    clear_button = Button(frame, image=clear_image, command=lambda: chat_box.config(state=NORMAL) or chat_box.delete(1.0, END) or chat_box.config(state=DISABLED), bd=0, bg="skyblue", relief=RAISED, activebackground="lightblue")
    clear_button.grid(row=2, column=0, pady=10)

    # Configure column and row weights to ensure proper resizing
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=0)
    frame.grid_rowconfigure(2, weight=0)

    root.mainloop()

# Start assistant activation
if __name__ == "__main__":
    initialize_gui()



# # Start assistant activation
# if __name__ == "__main__":
#     initialize_gui()
#     # activate_assistant()