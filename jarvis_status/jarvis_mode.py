
def toggle_jarwis_mode(mode):
        from main import speak
        if mode == "sleep":
            speak("Now I will be in sleeping mode. I won't listen to any commands.")
        elif mode == "wake up":
            speak("I am now awake. Welcome back sir.")