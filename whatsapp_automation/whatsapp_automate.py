import pyautogui as pi
import time
import subprocess
import pywhatkit as kit
def open_whatsapp():
    from main import speak
    from main import take_user_input
    # pi.hotkey('win','up')
    # pi.moveTo(750,1050,1)
    pi.click(x=750, y = 1050, clicks = 1, interval =0, button ='left')
    time.sleep(1)
    pi.typewrite("whatsapp")
    time.sleep(1)
    # # pi.moveTo(730,270,1)
    pi.click(x=730, y = 270, clicks = 1, interval =0, button ='left')
    time.sleep(1)
    speak("Do you want to send message to anyone sir? If yes whom do you want to send?")
    choice = take_user_input()
    if any(keyword in choice.lower() for keyword in ("yes","yeah","i had to","can you open","can i see","i need to","search for","can you search","can you provide",
                                                     "search for the name","i have to","look for","seek for","search for","can you find","will you","can i have","search by typing")if choice is not None):
        speak("Ok sir, I am searching.")
        start_keywords = ["search for"," seek for","look for", "find", "to", "about","at","from","with", "for", "of", "by", "too","search", "on", "in", "off"]
        words = choice.lower().split()
        search_query = ""
        # # Iterate over words to extract search query
        for i, word in enumerate(words):
            if word in start_keywords:
                search_query = " ".join(words[i + 1:])
        
        pi.click(x=170, y = 140, clicks = 1, interval =0, button ='left')
        time.sleep(1)
        pi.write(search_query)
        time.sleep(1)
        # pi.moveTo(200,240)
        pi.click(x=200, y = 240, clicks = 1, interval =0, button ='left')
        time.sleep(1)
        speak("Is this the person whom you want to connect?")
        person = take_user_input()
        if any(keyword in person.lower() for keyword in ("yes","yeah","sure","of course","off course","ofcourse","okay","okey","yep","click")if person is not None):
            pi.click(x=700, y = 900, clicks = 1, interval =0, button ='left')
            time.sleep(1)
            speak("Can you say your message sir?")
            message = take_user_input()
            pi.write(message)
            speak("Can i send it sir?")
            final_ans = take_user_input()
            if any(keyword in final_ans.lower() for keyword in ("yes","yeah","sure","of course","off course","ofcourse","okay","okey","ok")if final_ans is not None):
                pi.press("enter")
                speak(f"Message sent sucessfully.")
            else:
                speak("Ok sir, message discarded.")
        else:
            speak("Sorry sir, I couldn't find the person. You can search manually from here.")

    else:
        speak("Ok as your wish sir.")


    # import pywhatkit as kit
    # import time
    # import subprocess
    # # Define contacts as a dictionary
    # # Function to open WhatsApp Web
    # def open_whatsapp_web():
    #     name = input("Enter the name of the contact (or type 'exit' to quit): ")
    #     if name.lower() == 'exit':
    #         return None
    #     search_url = 'https://web.whatsapp.com'
    #     chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    #     subprocess.Popen([chrome_path, search_url])
    #     time.sleep(12)  # Allow time for WhatsApp Web to load
    #     send_message(name)
    #     time.sleep(10)

    # # Function to send a message

    # def send_message(name):
    #     if name in contacts:
    #         phone_number = contacts[name]
    #         message = f"Hello, this is a test message."
    #         kit.sendwhatmsg_instantly(phone_number, message, 8, True, 1)
    #         print(f"Message sent to {name}.")
    #     else:
    #         print(f"Contact {name} not found in contacts.")

    # # Open WhatsApp Web
    # open_whatsapp_web()

    # # Input loop to send messages to multiple contacts  # Wait a bit before allowing the next message

    # '''c
    # youtube search bar-806,125
    # whatapp search bar- 271,22
