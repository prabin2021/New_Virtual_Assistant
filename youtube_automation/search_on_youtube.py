import speech_recognition as sr
import urllib.parse
import subprocess

def extract_search_query(query):
        # from main_function.main import speak
        start_keywords = ["search for","search","for"," seek for","look for", "find", "search that", "about","search about","show me","watch"]
        # Split the query into words
        words = query.lower().split()
        # Initialize search query
        search_query = ""
        # # Iterate over words to extract search query
        for i, word in enumerate(words):
            if word in start_keywords:
                search_query = " ".join(words[i + 1:])
        return search_query
        
def search_youtube(search_query):
        from main import speak
        try:
            speak(",Okay sir,I am working for it.")
            base_url = "https://www.youtube.com/results?search_query="
            query_encoded = urllib.parse.quote(search_query)
            search_url = base_url + query_encoded
            # webbrowser.open(search_url)
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            subprocess.Popen([chrome_path, search_url])
        except sr.RequestError:
            speak("Sorry, I can't perform this action right now")
        except Exception as e:
            print("An error occurred:", e)