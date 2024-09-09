import pyjokes

def tell_random_joke():
    from main import speak
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)
    return joke
